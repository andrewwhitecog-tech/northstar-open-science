"""
Unit tests verifying exact mathematical and physical constraints on the
Simulation Hypothesis across Bayesian statistics, quantum many-body complexity,
lattice gauge theory, gamma-ray polarimetry, Landauer thermodynamics, and
the Edge & Brown (2026) observer-centric / artificial-physics counter-arguments.
"""

import math
from pathlib import Path

from simulation_bounds_verifier import (
    PLANCK_LENGTH_M,
    compute_bostrom_and_kipping,
    compute_dissipative_allometric_and_noether_bounds,
    compute_natural_morphogenesis_and_resonance,
    compute_observer_centric_shortcut,
    compute_quantum_hilbert_wall,
    compute_spacetime_discretization_bounds,
    compute_thermodynamic_bounds,
    compute_variational_laplace_and_atp_bounds,
    generate_full_verification_report,
)


def test_bostrom_and_kipping_bayesian_bounds():
    res = compute_bostrom_and_kipping(f_p=1.0, f_i=1.0, n_sim_bar=1.0e9)
    assert res.bostrom_f_sim > 0.99999999
    assert res.kipping_p_base_given_no_progeny > 0.5
    assert res.kipping_p_sim_given_no_progeny < 0.5
    assert math.isclose(
        res.kipping_p_base_given_no_progeny + res.kipping_p_sim_given_no_progeny,
        1.0,
        rel_tol=1e-12,
    )
    assert res.kipping_p_sim_if_progeny_created > 0.99999999


def test_ringel_kovrizhin_quantum_hilbert_wall_and_shortcuts():
    res_266 = compute_quantum_hilbert_wall(266)
    assert res_266.log10_hilbert_dim > 80.0
    assert 265.0 < res_266.spins_matching_universe_atoms < 266.0

    res_300 = compute_quantum_hilbert_wall(300)
    assert math.isclose(res_300.log10_hilbert_dim, 90.308998699, rel_tol=1e-6)
    assert res_300.ratio_states_to_universe_atoms_log10 > 10.0
    # Native quantum hardware or lazy measurement collapse requires only 300 qubits/bits!
    assert res_300.native_qubits_required == 300
    assert res_300.lazy_measurement_outcome_bits == 300


def test_spacetime_discretization_bounds():
    res = compute_spacetime_discretization_bounds(
        uhecr_energy_ev=1.0e20,
        human_qcd_spacing_m=1.0e-16,
        integral_grb_bound_m=1.0e-48,
    )
    assert math.isclose(PLANCK_LENGTH_M, 1.616255e-35, rel_tol=1e-4)
    assert math.isclose(res.max_lattice_spacing_uhecr_m, 1.97327e-27, rel_tol=1e-4)
    assert res.integral_to_planck_ratio < 1.0e-12


def test_vazza_landauer_thermodynamic_bounds():
    res = compute_thermodynamic_bounds(temperature_k=2.725)
    assert math.isclose(res.landauer_bit_energy_j, 2.608e-23, rel_tol=1e-3)
    assert res.vazza_low_res_earth_power_w > 3.0e44
    assert res.vazza_power_in_solar_luminosities > 8.0e17
    assert res.vazza_power_in_milky_way_luminosities > 6.0e7


def test_observer_centric_shortcut_rebuttal():
    # Verifies that simulating only the 8 billion human brains/senses (Edge & Brown 2026)
    # cuts power by >10^41x compared to Vazza's brute-force planet simulation!
    res = compute_observer_centric_shortcut()
    assert math.isclose(res.total_humanity_neural_ops_s, 8.0e25, rel_tol=1e-9)
    assert 2000.0 < res.neural_sim_power_at_cmb_w < 2200.0  # ~2,086 Watts (a hair dryer!)
    assert 2.2 < res.sensory_only_power_at_room_temp_w < 2.4  # ~2.30 Watts (an LED bulb!)
    assert res.efficiency_gain_factor_vs_vazza_log10 > 41.0


def test_natural_morphogenesis_and_resonance():
    res = compute_natural_morphogenesis_and_resonance()
    assert math.isclose(res.golden_ratio_phi, 1.618033988749895, rel_tol=1e-12)
    assert math.isclose(res.golden_angle_deg, 137.50776405003785, rel_tol=1e-9)
    assert res.turing_trace_j < 0.0
    assert res.turing_det_j > 0.0
    assert res.turing_instability_verified is True
    assert res.turing_characteristic_wavelength > 0.0
    assert math.isclose(res.kuramoto_critical_coupling_kc, 0.5, rel_tol=1e-12)


def test_dissipative_allometric_and_noether_bounds():
    res = compute_dissipative_allometric_and_noether_bounds(3)
    assert math.isclose(res.rayleigh_benard_free_rac, 657.51136, rel_tol=1e-5)
    assert math.isclose(res.wbe_metabolic_exponent_alpha, 0.75, rel_tol=1e-12)
    assert math.isclose(res.wbe_heart_rate_exponent, -0.25, rel_tol=1e-12)
    assert math.isclose(res.wbe_lifespan_exponent, 0.25, rel_tol=1e-12)
    assert math.isclose(res.kolmogorov_wavenumber_exponent_b, -5.0 / 3.0, rel_tol=1e-12)


def test_laplace_orbital_resonance():
    res = compute_variational_laplace_and_atp_bounds()
    assert res.laplace_resonance_residual_deg_per_day < 1e-5


def test_atp_synthase_and_feynman_fresnel_bounds():
    res = compute_variational_laplace_and_atp_bounds()
    assert math.isclose(res.atp_step_angle_rad, 2.0 * math.pi / 3.0, rel_tol=1e-12)
    assert 0.99 < res.atp_thermodynamic_efficiency <= 1.0
    assert 1.8e-17 < res.macro_fresnel_zone_width_m < 1.9e-17


def test_generate_full_verification_report(tmp_path: Path):
    out = tmp_path / "receipt.json"
    report = generate_full_verification_report(out)
    assert out.exists()
    assert "edge_brown_observer_centric_shortcut" in report
    assert "turing_fibonacci_kuramoto_morphogenesis" in report
    assert "prigogine_wbe_kolmogorov_self_organization" in report
    assert "feynman_laplace_atp_synthase_bounds" in report
