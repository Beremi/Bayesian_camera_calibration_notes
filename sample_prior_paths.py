#!/usr/bin/env python3
"""Generate illustrative samples from the discretized trajectory prior used in the annex.

This script is intentionally simple and self-contained. It samples a short 4 s trajectory prior
at 60 Hz and writes:
- figures/prior_paths_3d.png
- figures/prior_pose_glyphs.png
- figures/prior_state_evolution.png
- prior_sample_parameters.json
- prior_sample_summary.json
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.spatial.transform import Rotation as R

OUTDIR = Path(__file__).resolve().parent
FIGDIR = OUTDIR / "figures"
FIGDIR.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.grid": True,
    "grid.alpha": 0.22,
    "grid.linewidth": 0.6,
})

PARAMS = {
    "dt_s": 1/60,
    "horizon_s": 4.0,
    "num_paths_3d": 8,
    "num_paths_state": 6,
    "sigma_p0_m": [0.01, 0.01, 0.01],
    "sigma_v0_mps": [0.03, 0.03, 0.03],
    "sigma_rpy0_deg": [2.0, 2.0, 3.0],
    "sigma_omega0_degps": [4.0, 4.0, 5.0],
    "sigma_lin_acc_process_mps2": 0.10,
    "sigma_ang_acc_process_degps2": 6.0,
    "sigma_bg0_degps": [0.20, 0.20, 0.20],
    "sigma_ba0_mps2": [0.03, 0.03, 0.03],
    "sigma_bg_rw_step_degps": 0.005,
    "sigma_ba_rw_step_mps2": 0.001,
}

PALETTE = list(plt.get_cmap("tab10").colors)

def sample_path(seed: int, params: dict):
    rng = np.random.default_rng(seed)
    dt = params["dt_s"]
    N = int(params["horizon_s"] / dt) + 1
    sig_p0 = np.array(params["sigma_p0_m"])
    sig_v0 = np.array(params["sigma_v0_mps"])
    sig_rpy0 = np.deg2rad(np.array(params["sigma_rpy0_deg"]))
    sig_omega0 = np.deg2rad(np.array(params["sigma_omega0_degps"]))
    sig_a = params["sigma_lin_acc_process_mps2"]
    sig_alpha = np.deg2rad(params["sigma_ang_acc_process_degps2"])
    sig_bg0 = np.deg2rad(np.array(params["sigma_bg0_degps"]))
    sig_ba0 = np.array(params["sigma_ba0_mps2"])
    sig_bg_rw = np.deg2rad(params["sigma_bg_rw_step_degps"])
    sig_ba_rw = params["sigma_ba_rw_step_mps2"]

    p = rng.normal(0, sig_p0)
    v = rng.normal(0, sig_v0)
    rot = R.from_euler("xyz", rng.normal(0, sig_rpy0))
    omega = rng.normal(0, sig_omega0)
    bg = rng.normal(0, sig_bg0)
    ba = rng.normal(0, sig_ba0)

    P = np.zeros((N, 3))
    V = np.zeros((N, 3))
    RPY = np.zeros((N, 3))
    BG = np.zeros((N, 3))
    BA = np.zeros((N, 3))

    for k in range(N):
        P[k] = p
        V[k] = v
        BG[k] = bg
        BA[k] = ba
        RPY[k] = rot.as_euler("xyz", degrees=True)

        a = rng.normal(0, sig_a, size=3)
        alpha = rng.normal(0, sig_alpha, size=3)

        p = p + v * dt + 0.5 * a * dt ** 2
        v = v + a * dt
        rot = rot * R.from_rotvec(omega * dt)
        omega = omega + alpha * dt
        bg = bg + rng.normal(0, sig_bg_rw, size=3)
        ba = ba + rng.normal(0, sig_ba_rw, size=3)

    RPY = np.rad2deg(np.unwrap(np.deg2rad(RPY), axis=0))
    return {"p": P, "v": V, "rpy": RPY, "bg": BG, "ba": BA}

def main():
    (OUTDIR / "prior_sample_parameters.json").write_text(json.dumps(PARAMS, indent=2))
    paths = [sample_path(100 + i, PARAMS) for i in range(max(PARAMS["num_paths_3d"], PARAMS["num_paths_state"]))]

    dt = PARAMS["dt_s"]
    N = int(PARAMS["horizon_s"] / dt) + 1
    t = np.arange(N) * dt

    # 3D paths
    fig = plt.figure(figsize=(8.0, 6.2))
    ax = fig.add_subplot(111, projection="3d")
    for i, path in enumerate(paths[:PARAMS["num_paths_3d"]]):
        P = path["p"]
        color = PALETTE[i % len(PALETTE)]
        ax.plot(P[:, 0], P[:, 1], P[:, 2], color=color, linewidth=1.8, alpha=0.95, label=f"sample {i+1}")
        ax.scatter(P[0, 0], P[0, 1], P[0, 2], s=16, color=color)
    allP = np.concatenate([p["p"] for p in paths[:PARAMS["num_paths_3d"]]], axis=0)
    mins = allP.min(axis=0)
    maxs = allP.max(axis=0)
    center = 0.5 * (mins + maxs)
    span = 0.55 * (maxs - mins).max()
    ax.set_xlim(center[0] - span, center[0] + span)
    ax.set_ylim(center[1] - span, center[1] + span)
    ax.set_zlim(center[2] - span, center[2] + span)
    ax.set_xlabel("$p_x$ [m]")
    ax.set_ylabel("$p_y$ [m]")
    ax.set_zlabel("$p_z$ [m]")
    ax.set_box_aspect((1.0, 1.0, 0.8))
    ax.legend(loc="upper left", frameon=False, ncol=2)
    ax.view_init(elev=24, azim=-55)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(FIGDIR / "prior_paths_3d.png", dpi=240, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

    # Pose glyphs
    fig = plt.figure(figsize=(8.0, 6.2))
    ax = fig.add_subplot(111, projection="3d")
    path = paths[0]
    P = path["p"]
    ax.plot(P[:, 0], P[:, 1], P[:, 2], linewidth=2.0, color=PALETTE[0])
    for idx in np.linspace(0, N - 1, 10, dtype=int):
        rot = R.from_euler("xyz", path["rpy"][idx], degrees=True)
        basis = rot.as_matrix()
        p = P[idx]
        scale = 0.025
        axis_colors = ["#C0392B", "#2E8B57", "#2E5CB8"]
        for j, axis_color in enumerate(axis_colors):
            v = basis[:, j] * scale
            ax.quiver(
                p[0], p[1], p[2], v[0], v[1], v[2],
                arrow_length_ratio=0.2, linewidth=1.0, color=axis_color
            )
    ax.scatter(P[0, 0], P[0, 1], P[0, 2], s=30, color="black")
    mins = P.min(axis=0)
    maxs = P.max(axis=0)
    center = 0.5 * (mins + maxs)
    span = max(0.6 * (maxs - mins).max(), 0.08)
    ax.set_xlim(center[0] - span, center[0] + span)
    ax.set_ylim(center[1] - span, center[1] + span)
    ax.set_zlim(center[2] - span, center[2] + span)
    ax.set_xlabel("$p_x$ [m]")
    ax.set_ylabel("$p_y$ [m]")
    ax.set_zlabel("$p_z$ [m]")
    ax.set_box_aspect((1.0, 1.0, 0.8))
    ax.view_init(elev=24, azim=-55)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(FIGDIR / "prior_pose_glyphs.png", dpi=240, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

    # State evolution
    fig = plt.figure(figsize=(10.0, 12.0))
    gs = GridSpec(5, 3, figure=fig, hspace=0.35, wspace=0.22)
    labels = [
        (("p", "p_x [m]"), ("p", "p_y [m]"), ("p", "p_z [m]")),
        (("v", "v_x [m/s]"), ("v", "v_y [m/s]"), ("v", "v_z [m/s]")),
        (("rpy", "roll [deg]"), ("rpy", "pitch [deg]"), ("rpy", "yaw [deg]")),
        (("bg", "b_{g,x} [deg/s]"), ("bg", "b_{g,y} [deg/s]"), ("bg", "b_{g,z} [deg/s]")),
        (("ba", "b_{a,x} [m/s^2]"), ("ba", "b_{a,y} [m/s^2]"), ("ba", "b_{a,z} [m/s^2]")),
    ]
    for r in range(5):
        for c in range(3):
            ax = fig.add_subplot(gs[r, c])
            key, ylabel = labels[r][c]
            for i, path in enumerate(paths[:PARAMS["num_paths_state"]]):
                arr = path[key][:, c].copy()
                if key == "bg":
                    arr = np.rad2deg(arr)
                ax.plot(t, arr, linewidth=1.15, alpha=0.88, color=PALETTE[i % len(PALETTE)])
            ax.set_ylabel(ylabel, fontsize=9)
            if r == 0:
                ax.set_title(["x component", "y component", "z component"][c], fontsize=10)
            if r == 4:
                ax.set_xlabel("time [s]")
            ax.grid(True, alpha=0.22)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.97, hspace=0.35, wspace=0.22)
    fig.savefig(FIGDIR / "prior_state_evolution.png", dpi=240, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

    summary = {
        "horizon_s": PARAMS["horizon_s"],
        "num_samples": PARAMS["num_paths_3d"],
        "median_max_translation_excursion_m": float(np.median([np.linalg.norm(p["p"] - p["p"][0], axis=1).max() for p in paths[:PARAMS["num_paths_3d"]]])),
        "median_max_orientation_excursion_deg": float(np.median([np.abs(p["rpy"] - p["rpy"][0]).max() for p in paths[:PARAMS["num_paths_3d"]]])),
    }
    (OUTDIR / "prior_sample_summary.json").write_text(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
