"""
Quantitative Physics, Information Theory, and Bayesian Verification Suite
for the Simulation Hypothesis ("The Matrix" / Simulated Reality Investigation).

Computes and verifies exact equations from primary peer-reviewed literature:
1. Bostrom (2003), Philosophical Quarterly 53(211): 243-255.
2. Kipping (2020), Universe 6(8), 109 (arXiv:2006.03692).
3. Ringel & Kovrizhin (2017), Science Advances 3(9): e1701758.
4. Beane, Davoudi, & Savage (2014), European Physical Journal A 50, 148 (arXiv:1210.1847).
5. Laurent et al. (2011), Physical Review D 83, 121301(R) (arXiv:1106.1068).
6. Lloyd (2002), Physical Review Letters 88(23), 237901 (arXiv:quant-ph/0110141).
7. Vazza (2025), arXiv:2504.08461 (Astrophysical & Landauer thermodynamic bounds).
8. Edge & Brown (2026), Frontiers in Physics (Observer-centric / sensory rendering critique
   of Vazza 2025) & Bennett (1973) Reversible Computation.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

# Fundamental Physical Constants (CODATA 2022 / SI)
HBAR_J_S = 1.054571817e-34          # Reduced Planck constant (J * s)
HBAR_EV_S = 6.582119569e-16         # Reduced Planck constant (eV * s)
HBAR_C_EV_M = 1.973269804e-7        # hbar * c (eV * m)
C_M_S = 299792458.0                 # Speed of light in vacuum (m / s)
G_SI = 6.67430e-11                  # Gravitational constant (m^3 kg^-1 s^-2)
K_B_J_K = 1.380649e-23              # Boltzmann constant (J / K)
PLANCK_LENGTH_M = math.sqrt(HBAR_J_S * G_SI / (C_M_S ** 3))
PLANCK_TIME_S = PLANCK_LENGTH_M / C_M_S
OBSERVABLE_UNIVERSE_ATOMS = 1.0e80  # Estimated baryons in observable universe
SOLAR_LUMINOSITY_W = 3.828e26       # Solar luminosity (W)
MILKY_WAY_LUMINOSITY_W = 5.0e36     # Approximate bolometric luminosity of Milky Way (W)


@dataclass(frozen=True)
class BostromKippingResult:
    f_p: float
    f_i: float
    n_sim_bar: float
    bostrom_f_sim: float
    kipping_p_base_given_no_progeny: float
    kipping_p_sim_given_no_progeny: float
    kipping_p_base_if_progeny_created: float
    kipping_p_sim_if_progeny_created: float


def compute_bostrom_and_kipping(
    f_p: float = 1.0,
    f_i: float = 1.0,
    n_sim_bar: float = 1.0e9,
) -> BostromKippingResult:
    """
    Computes Nick Bostrom's (2003) fraction of simulated observers f_sim
    and David Kipping's (2020) Bayesian posterior probabilities.
    """
    if f_p < 0.0 or f_i < 0.0 or n_sim_bar < 0.0:
        raise ValueError("Parameters must be non-negative.")

    product = f_p * f_i * n_sim_bar
    bostrom_f_sim = product / (product + 1.0) if product > 0 else 0.0

    p_base_no_progeny = 0.5 + 0.5 / (n_sim_bar + 1.0)
    p_sim_no_progeny = 0.5 - 0.5 / (n_sim_bar + 1.0)

    p_base_with_progeny = 1.0 / (n_sim_bar + 1.0)
    p_sim_with_progeny = n_sim_bar / (n_sim_bar + 1.0)

    return BostromKippingResult(
        f_p=f_p,
        f_i=f_i,
        n_sim_bar=n_sim_bar,
        bostrom_f_sim=bostrom_f_sim,
        kipping_p_base_given_no_progeny=p_base_no_progeny,
        kipping_p_sim_given_no_progeny=p_sim_no_progeny,
        kipping_p_base_if_progeny_created=p_base_with_progeny,
        kipping_p_sim_if_progeny_created=p_sim_with_progeny,
    )


@dataclass(frozen=True)
class QuantumComplexityResult:
    n_spins: int
    log10_hilbert_dim: float
    log10_bytes_required: float
    ratio_states_to_universe_atoms_log10: float
    spins_matching_universe_atoms: float
    native_qubits_required: int
    lazy_measurement_outcome_bits: int


def compute_quantum_hilbert_wall(n_spins: int = 300) -> QuantumComplexityResult:
    """
    Computes the classical memory required to store the exact many-body quantum
    wavefunction of N spin-1/2 particles (Ringel & Kovrizhin 2017, Science Advances),
    and contrasts it with:
    (a) a native quantum computer (requiring only N qubits), and
    (b) lazy / on-demand measurement collapse (requiring only N outcome bits).
    """
    if n_spins < 1:
        raise ValueError("n_spins must be >= 1")

    log10_hilbert_dim = n_spins * math.log10(2.0)
    log10_bytes = log10_hilbert_dim + math.log10(16.0)
    log10_atoms = math.log10(OBSERVABLE_UNIVERSE_ATOMS)
    ratio_log10 = log10_hilbert_dim - log10_atoms
    spins_for_atoms = log10_atoms / math.log10(2.0)

    return QuantumComplexityResult(
        n_spins=n_spins,
        log10_hilbert_dim=log10_hilbert_dim,
        log10_bytes_required=log10_bytes,
        ratio_states_to_universe_atoms_log10=ratio_log10,
        spins_matching_universe_atoms=spins_for_atoms,
        native_qubits_required=n_spins,
        lazy_measurement_outcome_bits=n_spins,
    )


@dataclass(frozen=True)
class LatticeSpacetimeResult:
    uhecr_cutoff_energy_ev: float
    max_lattice_spacing_uhecr_m: float
    human_lattice_qcd_spacing_m: float
    resolution_gap_uhecr_vs_human_qcd: float
    integral_grb_bound_m: float
    planck_length_m: float
    integral_to_planck_ratio: float


def compute_spacetime_discretization_bounds(
    uhecr_energy_ev: float = 1.0e20,
    human_qcd_spacing_m: float = 1.0e-16,
    integral_grb_bound_m: float = 1.0e-48,
) -> LatticeSpacetimeResult:
    """
    Computes spacetime lattice bounds from:
    - Beane, Davoudi, & Savage (2014): b <= hbar * c / E_max for UHECRs (~10^20 eV).
    - Laurent et al. (2011) INTEGRAL GRB 041219A vacuum birefringence bound (~10^-48 m).
    """
    max_b_uhecr_m = HBAR_C_EV_M / uhecr_energy_ev
    resolution_gap = human_qcd_spacing_m / max_b_uhecr_m
    integral_to_planck = integral_grb_bound_m / PLANCK_LENGTH_M

    return LatticeSpacetimeResult(
        uhecr_cutoff_energy_ev=uhecr_energy_ev,
        max_lattice_spacing_uhecr_m=max_b_uhecr_m,
        human_lattice_qcd_spacing_m=human_qcd_spacing_m,
        resolution_gap_uhecr_vs_human_qcd=resolution_gap,
        integral_grb_bound_m=integral_grb_bound_m,
        planck_length_m=PLANCK_LENGTH_M,
        integral_to_planck_ratio=integral_to_planck,
    )


@dataclass(frozen=True)
class ThermodynamicBoundsResult:
    temperature_k: float
    landauer_bit_energy_j: float
    vazza_low_res_earth_bits: float
    vazza_low_res_earth_ops_per_s: float
    vazza_low_res_earth_power_w: float
    vazza_power_in_solar_luminosities: float
    vazza_power_in_milky_way_luminosities: float
    lloyd_universe_max_ops: float
    lloyd_universe_matter_bits: float
    lloyd_universe_holographic_bits: float


def compute_thermodynamic_bounds(
    temperature_k: float = 2.725,  # Cosmic Microwave Background temperature (K)
) -> ThermodynamicBoundsResult:
    """
    Computes Landauer energy dissipation bounds (Delta E >= k_B * T * ln 2)
    applied to Franco Vazza's (2025, arXiv:2504.08461) low-resolution Earth
    simulation benchmark (1.65e51 active bits, ~1.3e67 bit operations/s)
    and Seth Lloyd's (2002) computational capacity of the universe.
    """
    if temperature_k <= 0.0:
        raise ValueError("Temperature must be positive (Kelvin).")

    landauer_j = K_B_J_K * temperature_k * math.log(2.0)
    vazza_bits = 1.65e51
    vazza_ops_s = 1.30e67
    vazza_power_w = vazza_ops_s * landauer_j

    return ThermodynamicBoundsResult(
        temperature_k=temperature_k,
        landauer_bit_energy_j=landauer_j,
        vazza_low_res_earth_bits=vazza_bits,
        vazza_low_res_earth_ops_per_s=vazza_ops_s,
        vazza_low_res_earth_power_w=vazza_power_w,
        vazza_power_in_solar_luminosities=vazza_power_w / SOLAR_LUMINOSITY_W,
        vazza_power_in_milky_way_luminosities=vazza_power_w / MILKY_WAY_LUMINOSITY_W,
        lloyd_universe_max_ops=1.0e120,
        lloyd_universe_matter_bits=1.0e90,
        lloyd_universe_holographic_bits=1.0e122,
    )


@dataclass(frozen=True)
class ObserverCentricShortcutResult:
    human_population: float
    synaptic_ops_per_brain_s: float
    sensory_bits_per_human_s: float
    total_humanity_neural_ops_s: float
    total_humanity_sensory_bits_s: float
    neural_sim_power_at_cmb_w: float
    neural_sim_power_at_room_temp_w: float
    sensory_only_power_at_room_temp_w: float
    efficiency_gain_factor_vs_vazza_log10: float


def compute_observer_centric_shortcut(
    human_population: float = 8.0e9,
    synaptic_ops_per_brain_s: float = 1.0e16,
    sensory_bits_per_human_s: float = 1.0e11,
) -> ObserverCentricShortcutResult:
    """
    Quantifies the 'Less Sophisticated / Observer-Centric Simulation' counter-argument
    (Edge & Brown 2026, Frontiers in Physics; Bostrom 2003; Hoffman 2015).
    Instead of brute-forcing every neutrino in Earth's interior (Vazza 2025: 1.3e67 ops/s),
    an observer-centric simulation only computes the neural/sensory states of conscious
    observers and procedurally generates external measurements on demand.
    """
    total_neural_ops_s = human_population * synaptic_ops_per_brain_s
    total_sensory_bits_s = human_population * sensory_bits_per_human_s

    e_bit_cmb = K_B_J_K * 2.725 * math.log(2.0)
    e_bit_room = K_B_J_K * 300.0 * math.log(2.0)

    neural_power_cmb_w = total_neural_ops_s * e_bit_cmb
    neural_power_room_w = total_neural_ops_s * e_bit_room
    sensory_power_room_w = total_sensory_bits_s * e_bit_room

    vazza_ops_s = 1.30e67
    efficiency_gain_log10 = math.log10(vazza_ops_s / total_neural_ops_s)

    return ObserverCentricShortcutResult(
        human_population=human_population,
        synaptic_ops_per_brain_s=synaptic_ops_per_brain_s,
        sensory_bits_per_human_s=sensory_bits_per_human_s,
        total_humanity_neural_ops_s=total_neural_ops_s,
        total_humanity_sensory_bits_s=total_sensory_bits_s,
        neural_sim_power_at_cmb_w=neural_power_cmb_w,
        neural_sim_power_at_room_temp_w=neural_power_room_w,
        sensory_only_power_at_room_temp_w=sensory_power_room_w,
        efficiency_gain_factor_vs_vazza_log10=efficiency_gain_log10,
    )


@dataclass(frozen=True)
class NaturalMorphogenesisAndResonanceResult:
    golden_ratio_phi: float
    golden_angle_rad: float
    golden_angle_deg: float
    turing_trace_j: float
    turing_det_j: float
    turing_critical_wavenumber_sq: float
    turing_characteristic_wavelength: float
    turing_instability_verified: bool
    kuramoto_lorentzian_half_width_gamma: float
    kuramoto_critical_coupling_kc: float


def compute_natural_morphogenesis_and_resonance(
    f_u: float = 1.0,
    f_v: float = -2.0,
    g_u: float = 1.5,
    g_v: float = -1.5,
    d_u: float = 1.0,
    d_v: float = 10.0,
    kuramoto_gamma: float = 0.25,
) -> NaturalMorphogenesisAndResonanceResult:
    """
    Quantifies grounded physical self-organization in nature:
    1. Fibonacci Phyllotaxis (Douady & Couder 1992, PRL 68, 2098; Vogel 1979):
       Golden ratio phi = (1 + sqrt(5))/2 and golden divergence angle 2*pi*(2 - phi).
    2. Turing Reaction-Diffusion Morphogenesis (Turing 1952, Phil. Trans. R. Soc. B 237, 37):
       Homogeneous steady state is stable without diffusion (Tr(J) < 0, det(J) > 0)
       but unstable to spatial wavenumber k_c^2 = (d_v*f_u + d_u*g_v)/(2*d_u*d_v) > 0
       when (d_v*f_u + d_u*g_v) > 2*sqrt(d_u*d_v*det(J)).
    3. Huygens-Kuramoto Coupled Oscillator Synchronization (Huygens 1665; Kuramoto 1975):
       For a Lorentzian natural frequency distribution g(omega) = (gamma/pi)/(omega^2 + gamma^2),
       the exact critical coupling for spontaneous phase-locking is K_c = 2 / (pi * g(0)) = 2 * gamma.
    """
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    golden_rad = 2.0 * math.pi * (2.0 - phi)
    golden_deg = math.degrees(golden_rad)

    tr_j = f_u + g_v
    det_j = f_u * g_v - f_v * g_u
    kc_sq = (d_v * f_u + d_u * g_v) / (2.0 * d_u * d_v)
    wavelength = (2.0 * math.pi) / math.sqrt(kc_sq)
    instability_ok = (
        (tr_j < 0.0)
        and (det_j > 0.0)
        and ((d_v * f_u + d_u * g_v) > 2.0 * math.sqrt(d_u * d_v * det_j))
    )

    kc = 2.0 * kuramoto_gamma

    return NaturalMorphogenesisAndResonanceResult(
        golden_ratio_phi=phi,
        golden_angle_rad=golden_rad,
        golden_angle_deg=golden_deg,
        turing_trace_j=tr_j,
        turing_det_j=det_j,
        turing_critical_wavenumber_sq=kc_sq,
        turing_characteristic_wavelength=wavelength,
        turing_instability_verified=instability_ok,
        kuramoto_lorentzian_half_width_gamma=kuramoto_gamma,
        kuramoto_critical_coupling_kc=kc,
    )


@dataclass(frozen=True)
class DissipativeAllometricBoundsResult:
    rayleigh_benard_free_kc: float
    rayleigh_benard_free_rac: float
    rayleigh_benard_rigid_rac: float
    spatial_dimension_d: int
    wbe_metabolic_exponent_alpha: float
    wbe_heart_rate_exponent: float
    wbe_lifespan_exponent: float
    kolmogorov_dissipation_exponent_a: float
    kolmogorov_wavenumber_exponent_b: float
    helmholtz_fifth_ratio: float
    helmholtz_major_third_ratio: float


def compute_dissipative_allometric_and_noether_bounds(
    spatial_dimension_d: int = 3,
) -> DissipativeAllometricBoundsResult:
    """
    Quantifies universal non-equilibrium self-organization, fractal allometry,
    turbulence scaling, and acoustic harmonic ratios:
    1. Rayleigh-Benard Convection (Lord Rayleigh 1916; Prigogine 1977 Nobel Lecture):
       Stress-free critical wavenumber k_c = pi/sqrt(2) and Ra_c = 27*pi^4 / 4.
    2. West-Brown-Enquist Fractal Allometry (West, Brown, & Enquist 1997, Science 276, 122):
       Metabolic scaling exponent alpha = D / (D + 1) = 3/4 in D=3 spatial dimensions.
    3. Kolmogorov 1941 Turbulence Cascade (Dokl. Akad. Nauk SSSR 30, 299):
       E(k) = C_K * epsilon^(2/3) * k^(-5/3).
    4. Helmholtz (1863) Just Intonation Overtone Consonance Ratios:
       Perfect fifth = 3/2, Major third = 5/4.
    """
    kc_free = math.pi / math.sqrt(2.0)
    rac_free = 27.0 * (math.pi ** 4) / 4.0
    rac_rigid = 1707.761777

    alpha_wbe = spatial_dimension_d / float(spatial_dimension_d + 1)
    heart_exp = -1.0 / float(spatial_dimension_d + 1)
    life_exp = 1.0 / float(spatial_dimension_d + 1)

    return DissipativeAllometricBoundsResult(
        rayleigh_benard_free_kc=kc_free,
        rayleigh_benard_free_rac=rac_free,
        rayleigh_benard_rigid_rac=rac_rigid,
        spatial_dimension_d=spatial_dimension_d,
        wbe_metabolic_exponent_alpha=alpha_wbe,
        wbe_heart_rate_exponent=heart_exp,
        wbe_lifespan_exponent=life_exp,
        kolmogorov_dissipation_exponent_a=2.0 / 3.0,
        kolmogorov_wavenumber_exponent_b=-5.0 / 3.0,
        helmholtz_fifth_ratio=1.5,
        helmholtz_major_third_ratio=1.25,
    )


@dataclass(frozen=True)
class VariationalLaplaceAndAtpResult:
    io_mean_motion_deg_per_day: float
    europa_mean_motion_deg_per_day: float
    ganymede_mean_motion_deg_per_day: float
    laplace_resonance_residual_deg_per_day: float
    atp_step_angle_rad: float
    atp_stall_torque_pn_nm: float
    atp_mechanical_work_pn_nm: float
    atp_free_energy_pn_nm: float
    atp_thermodynamic_efficiency: float
    macro_fresnel_zone_width_m: float


def compute_variational_laplace_and_atp_bounds(
    atp_stall_torque_pn_nm: float = 41.2,
    atp_free_energy_pn_nm: float = 86.3,
) -> VariationalLaplaceAndAtpResult:
    """
    Quantifies:
    1. Laplace 4:2:1 Three-Body Orbital Resonance (Laplace 1799; Peale 1976):
       n_Io - 3*n_Europa + 2*n_Ganymede = 0 using observed synodic/sidereal mean motions.
    2. F0F1-ATP Synthase Rotary Nanomotor Efficiency (Boyer & Walker 1997 Nobel Prize;
       Yasuda, Noji, Kinosita, & Yoshida 1998, Cell 93, 1117):
       120-degree (2*pi/3 rad) rotary step at ~41.2 pN*nm stall torque yields W = tau * (2*pi/3)
       ~ 86.29 pN*nm, matching Delta G_ATP (~86.3 pN*nm) at ~99.9% thermodynamic efficiency.
    3. Feynman Path Integral Stationary Phase Fresnel Width (Feynman 1948, RMP 20, 367):
       Delta x = sqrt(pi * hbar * t / m) for a 1 kg mass over 1 second (~1.82e-17 m).
    """
    # Exact sidereal mean motions (deg/day) of Galilean satellites (Showman & Malhotra 1999)
    n_io = 203.4889538
    n_eu = 101.3747235
    n_ga = 50.3176081
    laplace_res = abs(n_io - 3.0 * n_eu + 2.0 * n_ga)

    step_rad = 2.0 * math.pi / 3.0
    work_pn_nm = atp_stall_torque_pn_nm * step_rad
    efficiency = work_pn_nm / atp_free_energy_pn_nm

    fresnel_m = math.sqrt(math.pi * HBAR_J_S * 1.0 / 1.0)

    return VariationalLaplaceAndAtpResult(
        io_mean_motion_deg_per_day=n_io,
        europa_mean_motion_deg_per_day=n_eu,
        ganymede_mean_motion_deg_per_day=n_ga,
        laplace_resonance_residual_deg_per_day=laplace_res,
        atp_step_angle_rad=step_rad,
        atp_stall_torque_pn_nm=atp_stall_torque_pn_nm,
        atp_mechanical_work_pn_nm=work_pn_nm,
        atp_free_energy_pn_nm=atp_free_energy_pn_nm,
        atp_thermodynamic_efficiency=efficiency,
        macro_fresnel_zone_width_m=fresnel_m,
    )


def generate_full_verification_report(output_path: Path | None = None) -> dict:
    """Generates a complete JSON-serializable report of all physical and shortcut bounds."""
    bk = compute_bostrom_and_kipping()
    qc = compute_quantum_hilbert_wall(300)
    lat = compute_spacetime_discretization_bounds()
    thermo = compute_thermodynamic_bounds(2.725)
    shortcut = compute_observer_centric_shortcut()
    morph = compute_natural_morphogenesis_and_resonance()
    diss = compute_dissipative_allometric_and_noether_bounds(3)
    var_atp = compute_variational_laplace_and_atp_bounds()

    report = {
        "constants": {
            "planck_length_m": PLANCK_LENGTH_M,
            "planck_time_s": PLANCK_TIME_S,
            "observable_universe_atoms": OBSERVABLE_UNIVERSE_ATOMS,
            "cmb_temperature_k": 2.725,
        },
        "bostrom_kipping_bayesian": asdict(bk),
        "ringel_kovrizhin_quantum_wall": asdict(qc),
        "beane_laurent_lattice_bounds": asdict(lat),
        "vazza_lloyd_thermodynamic_bounds": asdict(thermo),
        "edge_brown_observer_centric_shortcut": asdict(shortcut),
        "turing_fibonacci_kuramoto_morphogenesis": asdict(morph),
        "prigogine_wbe_kolmogorov_self_organization": asdict(diss),
        "feynman_laplace_atp_synthase_bounds": asdict(var_atp),
    }

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    return report


if __name__ == "__main__":
    out_file = Path(__file__).parent / "simulation_bounds_receipt.json"
    data = generate_full_verification_report(out_file)
    print(json.dumps(data, indent=2))
