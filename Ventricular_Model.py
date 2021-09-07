# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:17:00 2021

Ventricular version

@author: Alonso, M. - 2021 hiPSC model
"""

# Size of variable arrays:
sizeAlgebraic = 71
sizeStates = 27
sizeConstants = 93
from math import *
from numpy import *


def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Vm in component Membrane (volt)"
    legend_algebraic[52] = "i_CaL in component i_CaL (A_per_F)"
    legend_algebraic[58] = "i_K1 in component i_K1 (A_per_F)"
    legend_algebraic[59] = "i_f in component i_f (A_per_F)"
    legend_algebraic[51] = "i_Na in component i_Na (A_per_F)"
    legend_algebraic[53] = "i_Kr in component i_Kr (A_per_F)"
    legend_algebraic[54] = "i_Ks in component i_Ks (A_per_F)"
    legend_algebraic[65] = "i_to in component i_to (A_per_F)"
    legend_algebraic[64] = "i_PCa in component i_PCa (A_per_F)"
    legend_algebraic[62] = "i_NaK in component i_NaK (A_per_F)"
    legend_algebraic[63] = "i_NaCa in component i_NaCa (A_per_F)"
    legend_algebraic[61] = "i_b_Ca in component i_b_Ca (A_per_F)"
    legend_algebraic[60] = "i_b_Na in component i_b_Na (A_per_F)"
    legend_algebraic[10] = "i_stim in component stim_mode (A_per_F)"
    legend_constants[0] = "Cm in component model_parameters (farad)"
    legend_constants[1] = "stim_flag in component stim_mode (dimensionless)"
    legend_constants[2] = "i_stim_Start in component stim_mode (second)"
    legend_constants[3] = "i_stim_End in component stim_mode (second)"
    legend_constants[4] = "i_stim_Amplitude in component stim_mode (ampere)"
    legend_constants[5] = "i_stim_frequency in component stim_mode (per_second)"
    legend_constants[65] = "i_stim_Period in component stim_mode (second)"
    legend_constants[6] = "i_stim_PulseDuration in component stim_mode (second)"
    legend_constants[7] = "TTX_3uM in component current_blockers (dimensionless)"
    legend_constants[8] = "TTX_10uM in component current_blockers (dimensionless)"
    legend_constants[9] = "TTX_30uM in component current_blockers (dimensionless)"
    legend_constants[10] = "E4031_30nM in component current_blockers (dimensionless)"
    legend_constants[11] = "E4031_100nM in component current_blockers (dimensionless)"
    legend_constants[12] = "nifed_3nM in component current_blockers (dimensionless)"
    legend_constants[13] = "nifed_10nM in component current_blockers (dimensionless)"
    legend_constants[14] = "nifed_30nM in component current_blockers (dimensionless)"
    legend_constants[15] = "nifed_100nM in component current_blockers (dimensionless)"
    legend_constants[16] = "Chromanol_iKs30 in component current_blockers (dimensionless)"
    legend_constants[17] = "Chromanol_iKs50 in component current_blockers (dimensionless)"
    legend_constants[18] = "Chromanol_iKs70 in component current_blockers (dimensionless)"
    legend_constants[19] = "Chromanol_iKs90 in component current_blockers (dimensionless)"
    legend_algebraic[25] = "E_Na in component electric_potentials (volt)"
    legend_constants[66] = "E_K in component electric_potentials (volt)"
    legend_algebraic[39] = "E_Ks in component electric_potentials (volt)"
    legend_algebraic[48] = "E_Ca in component electric_potentials (volt)"
    legend_constants[20] = "R in component model_parameters (joule_per_mole_kelvin)"
    legend_constants[21] = "T in component model_parameters (kelvin)"
    legend_constants[22] = "F in component model_parameters (coulomb_per_mole)"
    legend_states[1] = "Nai in component sodium_dynamics (millimolar)"
    legend_constants[23] = "Nao in component model_parameters (millimolar)"
    legend_states[2] = "Cai in component calcium_dynamics (millimolar)"
    legend_constants[24] = "Cao in component model_parameters (millimolar)"
    legend_constants[25] = "Ki in component model_parameters (millimolar)"
    legend_constants[26] = "Ko in component model_parameters (millimolar)"
    legend_constants[27] = "PkNa in component electric_potentials (dimensionless)"
    legend_constants[28] = "g_Na in component i_Na (S_per_F)"
    legend_states[3] = "m in component i_Na_m_gate (dimensionless)"
    legend_states[4] = "h in component i_Na_h_gate (dimensionless)"
    legend_states[5] = "j in component i_Na_j_gate (dimensionless)"
    legend_constants[67] = "TTX_coeff in component i_Na (dimensionless)"
    legend_algebraic[0] = "m_inf in component i_Na_m_gate (dimensionless)"
    legend_algebraic[40] = "tau_m in component i_Na_m_gate (second)"
    legend_algebraic[15] = "alpha_m in component i_Na_m_gate (dimensionless)"
    legend_algebraic[30] = "beta_m in component i_Na_m_gate (dimensionless)"
    legend_algebraic[1] = "h_inf in component i_Na_h_gate (dimensionless)"
    legend_algebraic[16] = "alpha_h in component i_Na_h_gate (dimensionless)"
    legend_algebraic[31] = "beta_h in component i_Na_h_gate (dimensionless)"
    legend_algebraic[41] = "tau_h in component i_Na_h_gate (second)"
    legend_algebraic[2] = "j_inf in component i_Na_j_gate (dimensionless)"
    legend_algebraic[17] = "alpha_j in component i_Na_j_gate (dimensionless)"
    legend_algebraic[32] = "beta_j in component i_Na_j_gate (dimensionless)"
    legend_algebraic[42] = "tau_j in component i_Na_j_gate (second)"
    legend_constants[29] = "g_CaL in component i_CaL (metre_cube_per_F_per_s)"
    legend_states[6] = "d in component i_CaL_d_gate (dimensionless)"
    legend_states[7] = "f1 in component i_CaL_f1_gate (dimensionless)"
    legend_states[8] = "f2 in component i_CaL_f2_gate (dimensionless)"
    legend_states[9] = "fCa in component i_CaL_fCa_gate (dimensionless)"
    legend_constants[68] = "nifed_coeff in component i_CaL (dimensionless)"
    legend_algebraic[3] = "d_infinity in component i_CaL_d_gate (dimensionless)"
    legend_algebraic[49] = "tau_d in component i_CaL_d_gate (second)"
    legend_algebraic[18] = "alpha_d in component i_CaL_d_gate (dimensionless)"
    legend_algebraic[33] = "beta_d in component i_CaL_d_gate (dimensionless)"
    legend_algebraic[43] = "gamma_d in component i_CaL_d_gate (dimensionless)"
    legend_algebraic[4] = "f1_inf in component i_CaL_f1_gate (dimensionless)"
    legend_algebraic[34] = "tau_f1 in component i_CaL_f1_gate (second)"
    legend_algebraic[19] = "constf1 in component i_CaL_f1_gate (dimensionless)"
    legend_algebraic[5] = "f2_inf in component i_CaL_f2_gate (dimensionless)"
    legend_algebraic[20] = "tau_f2 in component i_CaL_f2_gate (second)"
    legend_constants[69] = "constf2 in component i_CaL_f2_gate (dimensionless)"
    legend_algebraic[50] = "constfCa in component i_CaL_fCa_gate (dimensionless)"
    legend_algebraic[6] = "alpha_fCa in component i_CaL_fCa_gate (dimensionless)"
    legend_algebraic[21] = "beta_fCa in component i_CaL_fCa_gate (dimensionless)"
    legend_algebraic[35] = "gamma_fCa in component i_CaL_fCa_gate (dimensionless)"
    legend_algebraic[44] = "fCa_inf in component i_CaL_fCa_gate (dimensionless)"
    legend_constants[30] = "tau_fCa in component i_CaL_fCa_gate (second)"
    legend_constants[31] = "g_Kr in component i_Kr (S_per_F)"
    legend_states[10] = "Xr1 in component i_Kr_Xr1_gate (dimensionless)"
    legend_states[11] = "Xr2 in component i_Kr_Xr2_gate (dimensionless)"
    legend_constants[70] = "E4031_coeff in component i_Kr (dimensionless)"
    legend_algebraic[7] = "Xr1_inf in component i_Kr_Xr1_gate (dimensionless)"
    legend_algebraic[22] = "alpha_Xr1 in component i_Kr_Xr1_gate (dimensionless)"
    legend_algebraic[36] = "beta_Xr1 in component i_Kr_Xr1_gate (dimensionless)"
    legend_algebraic[45] = "tau_Xr1 in component i_Kr_Xr1_gate (second)"
    legend_constants[32] = "L0 in component i_Kr_Xr1_gate (dimensionless)"
    legend_constants[71] = "V_half in component i_Kr_Xr1_gate (millivolt)"
    legend_constants[33] = "Q in component i_Kr_Xr1_gate (dimensionless)"
    legend_algebraic[8] = "Xr2_infinity in component i_Kr_Xr2_gate (dimensionless)"
    legend_algebraic[23] = "alpha_Xr2 in component i_Kr_Xr2_gate (dimensionless)"
    legend_algebraic[37] = "beta_Xr2 in component i_Kr_Xr2_gate (dimensionless)"
    legend_algebraic[46] = "tau_Xr2 in component i_Kr_Xr2_gate (second)"
    legend_constants[34] = "g_Ks in component i_Ks (S_per_F)"
    legend_states[12] = "Xs in component i_Ks_Xs_gate (dimensionless)"
    legend_constants[72] = "Chromanol_coeff in component i_Ks (dimensionless)"
    legend_algebraic[9] = "Xs_infinity in component i_Ks_Xs_gate (dimensionless)"
    legend_algebraic[24] = "alpha_Xs in component i_Ks_Xs_gate (dimensionless)"
    legend_algebraic[38] = "beta_Xs in component i_Ks_Xs_gate (dimensionless)"
    legend_algebraic[47] = "tau_Xs in component i_Ks_Xs_gate (second)"
    legend_constants[35] = "g_K1 in component i_K1 (S_per_F)"
    legend_algebraic[57] = "XK1_inf in component i_K1 (dimensionless)"
    legend_algebraic[55] = "alpha_K1 in component i_K1 (dimensionless)"
    legend_algebraic[56] = "beta_K1 in component i_K1 (dimensionless)"
    legend_constants[36] = "g_f in component i_f (S_per_F)"
    legend_constants[37] = "E_f in component i_f (volt)"
    legend_states[13] = "Xf in component i_f_Xf_gate (dimensionless)"
    legend_algebraic[11] = "Xf_infinity in component i_f_Xf_gate (dimensionless)"
    legend_algebraic[26] = "tau_Xf in component i_f_Xf_gate (second)"
    legend_constants[38] = "g_b_Na in component i_b_Na (S_per_F)"
    legend_constants[39] = "g_b_Ca in component i_b_Ca (S_per_F)"
    legend_constants[40] = "Km_K in component i_NaK (millimolar)"
    legend_constants[41] = "Km_Na in component i_NaK (millimolar)"
    legend_constants[42] = "PNaK in component i_NaK (A_per_F)"
    legend_constants[43] = "kNaCa in component i_NaCa (A_per_F)"
    legend_constants[44] = "alpha in component i_NaCa (dimensionless)"
    legend_constants[45] = "gamma in component i_NaCa (dimensionless)"
    legend_constants[46] = "Ksat in component i_NaCa (dimensionless)"
    legend_constants[47] = "KmCa in component i_NaCa (millimolar)"
    legend_constants[48] = "KmNai in component i_NaCa (millimolar)"
    legend_constants[49] = "g_PCa in component i_PCa (A_per_F)"
    legend_constants[50] = "KPCa in component i_PCa (millimolar)"
    legend_constants[51] = "g_to in component i_to (S_per_F)"
    legend_states[14] = "q in component i_to_q_gate (dimensionless)"
    legend_states[15] = "r in component i_to_r_gate (dimensionless)"
    legend_algebraic[12] = "q_inf in component i_to_q_gate (dimensionless)"
    legend_algebraic[27] = "tau_q in component i_to_q_gate (second)"
    legend_algebraic[13] = "r_inf in component i_to_r_gate (dimensionless)"
    legend_algebraic[28] = "tau_r in component i_to_r_gate (second)"
    legend_constants[52] = "Vc in component model_parameters (micrometre_cube)"
    legend_constants[53] = "V_SR in component model_parameters (micrometre_cube)"
    legend_states[16] = "Ca_SR in component calcium_dynamics (millimolar)"
    legend_constants[54] = "a_rel in component calcium_dynamics (millimolar_per_second)"
    legend_constants[55] = "b_rel in component calcium_dynamics (millimolar)"
    legend_constants[56] = "c_rel in component calcium_dynamics (millimolar_per_second)"
    legend_states[17] = "g in component calcium_dynamics (dimensionless)"
    legend_constants[57] = "tau_g in component calcium_dynamics (second)"
    legend_algebraic[14] = "g_inf in component calcium_dynamics (dimensionless)"
    legend_constants[58] = "Kup in component calcium_dynamics (millimolar)"
    legend_constants[59] = "Buf_C in component calcium_dynamics (millimolar)"
    legend_constants[60] = "Buf_SR in component calcium_dynamics (millimolar)"
    legend_constants[61] = "Kbuf_C in component calcium_dynamics (millimolar)"
    legend_constants[62] = "Kbuf_SR in component calcium_dynamics (millimolar)"
    legend_algebraic[69] = "Cai_bufc in component calcium_dynamics (dimensionless)"
    legend_algebraic[70] = "Ca_SR_bufSR in component calcium_dynamics (dimensionless)"
    legend_constants[63] = "VmaxUp in component calcium_dynamics (millimolar_per_second)"
    legend_algebraic[29] = "const2 in component calcium_dynamics (dimensionless)"
    legend_constants[64] = "V_leak in component calcium_dynamics (per_second)"
    legend_algebraic[66] = "j_rel in component calcium_dynamics (millimolar_per_second)"
    legend_algebraic[67] = "j_up in component calcium_dynamics (millimolar_per_second)"
    legend_algebraic[68] = "j_leak in component calcium_dynamics (millimolar_per_second)"
    legend_rates[0] = "d/dt Vm in component Membrane (volt)"
    legend_rates[3] = "d/dt m in component i_Na_m_gate (dimensionless)"
    legend_rates[4] = "d/dt h in component i_Na_h_gate (dimensionless)"
    legend_rates[5] = "d/dt j in component i_Na_j_gate (dimensionless)"
    legend_rates[6] = "d/dt d in component i_CaL_d_gate (dimensionless)"
    legend_rates[7] = "d/dt f1 in component i_CaL_f1_gate (dimensionless)"
    legend_rates[8] = "d/dt f2 in component i_CaL_f2_gate (dimensionless)"
    legend_rates[9] = "d/dt fCa in component i_CaL_fCa_gate (dimensionless)"
    legend_rates[10] = "d/dt Xr1 in component i_Kr_Xr1_gate (dimensionless)"
    legend_rates[11] = "d/dt Xr2 in component i_Kr_Xr2_gate (dimensionless)"
    legend_rates[12] = "d/dt Xs in component i_Ks_Xs_gate (dimensionless)"
    legend_rates[13] = "d/dt Xf in component i_f_Xf_gate (dimensionless)"
    legend_rates[14] = "d/dt q in component i_to_q_gate (dimensionless)"
    legend_rates[15] = "d/dt r in component i_to_r_gate (dimensionless)"
    legend_rates[1] = "d/dt Nai in component sodium_dynamics (millimolar)"
    legend_rates[17] = "d/dt g in component calcium_dynamics (dimensionless)"
    legend_rates[2] = "d/dt Cai in component calcium_dynamics (millimolar)"
    legend_rates[16] = "d/dt Ca_SR in component calcium_dynamics (millimolar)"
    
    # Dynamic Buffer components
    legend_states[18] = "SR in component calcium_dynamics (millimolar)"
    legend_rates[18] = "d/dt SR in component calcium_dynamics (millimolar)"
    legend_constants[73] = "Kbuf_on_SR in component calcium_dynamics (mM-1 s-1)"
    legend_constants[74] = "Kbuf_off_SR in component calcium_dynamics (s-1)"
    legend_constants[75] = "Buf_SR in component calcium_dynamics (millimolar)"
    legend_states[19] = "CAM in component calcium_dynamics (millimolar)"
    legend_rates[19] = "d/dt CAM in component calcium_dynamics (millimolar)"
    legend_constants[76] = "Kbuf_on_CAM in component calcium_dynamics (mM-1 s-1)"
    legend_constants[77] = "Kbuf_off_CAM in component calcium_dynamics (s-1)"
    legend_constants[78] = "Buf_CAM in component calcium_dynamics (millimolar)"
    legend_states[20] = "SLH in component calcium_dynamics (millimolar)"
    legend_rates[20] = "d/dt SLH in component calcium_dynamics (millimolar)"
    legend_constants[79] = "Kbuf_on_SLH in component calcium_dynamics (mM-1 s-1)"
    legend_constants[80] = "Kbuf_off_SLH in component calcium_dynamics (s-1)"
    legend_constants[81] = "Buf_SLH in component calcium_dynamics (millimolar)"
    legend_states[21] = "TnC in component calcium_dynamics (millimolar)"
    legend_rates[21] = "d/dt TnC in component calcium_dynamics (millimolar)"
    legend_constants[82] = "Kbuf_on_TnC in component calcium_dynamics (mM-1 s-1)"
    legend_constants[83] = "Kbuf_off_TnC in component calcium_dynamics (s-1)"
    legend_constants[84] = "Buf_TnC in component calcium_dynamics (millimolar)"
    legend_states[22] = "Rhod-2 in component calcium_dynamics (millimolar)"
    legend_rates[22] = "d/dt Rhod-2 in component calcium_dynamics (millimolar)"
    legend_constants[85] = "Kbuf_on_Rhod-2 in component calcium_dynamics (mM-1 s-1)"
    legend_constants[86] = "Kbuf_off_Rhod-2 in component calcium_dynamics (s-1)"
    legend_constants[87] = "Buf_Rhod-2 in component calcium_dynamics (millimolar)"
    
    # RyR scheme
    legend_constants[88] = "k_io and k_ic in component RyR scheme (ms-1)"
    legend_constants[89] = "Ci in component RyR scheme (micromolar)"
    legend_constants[90] = "k_oc and k_i1i2 in component RyR scheme (ms-1)"
    legend_constants[91] = "k_io and k_ic in component RyR scheme (ms-1)"
    legend_constants[92] = "g_rel in component j_rel (s-1)"
    
    legend_states[23] = "C - closed state of the RyR (s-1)"
    legend_states[24] = "R1- closed state of the RyR (s-1)"
    legend_states[25] = "R2 - closed state of the RyR (s-1)"
    legend_states[26] = "O - closed state of the RyR (s-1)"
    
    legend_rates[23] = "d/dt C - closed state of the RyR (s-1)"
    legend_rates[24] = "d/dt R1 - closed state of the RyR (s-1)"
    legend_rates[25] = "d/dt R2 - closed state of the RyR (s-1)"
    legend_rates[26] = "d/dt O - closed state of the RyR (s-1)"
    
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -0.0743340057623841
    constants[0] = 9.87109e-11            # cell capacitance
    
    # Stimulating current parameters 
    constants[1] = 0                      # stim flag
    constants[2] = 0                      # stim start 
    constants[3] = 800                    # stim end
    constants[4] = 1*constants[0]         # stim amplitude (ampere)
    constants[5] = 1                      # stim freq
    constants[6] = 0.005                  # pulse duration
    constants[65] = 1.0000/constants[5]   # stim period
    
    constants[7] = 0
    constants[8] = 0
    constants[9] = 0
    constants[10] = 0
    constants[11] = 0
    constants[12] = 0
    constants[13] = 0
    constants[14] = 0
    constants[15] = 0
    constants[16] = 0
    constants[17] = 0
    constants[18] = 0
    constants[19] = 0
    constants[20] = 8.314472
    constants[21] = 310
    constants[22] = 96485.3415
    states[1] = 9.991                     # initial sodium concentration 
    constants[23] = 151
    states[2] = 1.80773974140477e-5
    constants[24] = 1.8
    constants[25] = 150
    constants[26] = 5.4
    constants[27] = 0.03
    constants[28] = 3671.2302
    states[3] = 0.102953468725004
    states[4] = 0.786926637881461
    states[5] = 0.253943221774722
    constants[29] = 8.635702e-5
    states[6] = 8.96088425225182e-5
    states[7] = 0.970411811263976
    states[8] = 0.999965815466749
    states[9] = 0.998925296531804
    constants[30] = 0.002
    constants[31] = 29.8667
    states[10] = 0.00778547011240132
    states[11] = 0.432162576531617
    constants[32] = 0.025
    constants[33] = 2.3
    constants[34] = 2.041
    states[12] = 0.0322944866983666
    constants[35] = 28.1492
    constants[36] = 30.10312
    constants[37] = -0.017
    states[13] = 0.100615100568753
    constants[38] = 0.9
    constants[39] = 0.69264
    constants[40] = 1
    constants[41] = 40
    constants[42] = 1.841424
    constants[43] = 1633.3333
    constants[44] = 2.8571432
    constants[45] = 0.35
    constants[46] = 0.1
    constants[47] = 1.38
    constants[48] = 87.5
    constants[49] = 0.4125
    constants[50] = 0.0005
    constants[51] = 29.9038
    states[14] = 0.839295925773219
    states[15] = 0.00573289893326379
    constants[52] = 8800
    constants[53] = 583.73
    states[16] = 0.12                       # Ca SR initial concentration
    constants[54] = 16.464
    constants[55] = 0.25
    constants[56] = 8.232
    states[17] = 0.999999981028517
    constants[57] = 0.002
    constants[58] = 0.00025
    constants[59] = 0.25
    constants[60] = 10
    constants[61] = 0.001
    constants[62] = 0.3
    constants[63] = 0.728832
    constants[64] = 0.00044444
    constants[66] = ((constants[20]*constants[21])/constants[22])*log(constants[26]/constants[25])
    constants[67] = custom_piecewise([equal(constants[7] , 1.00000), 0.180000 , equal(constants[8] , 1.00000), 0.0600000 , equal(constants[9] , 1.00000), 0.0200000 , True, 1.00000])
    constants[68] = custom_piecewise([equal(constants[12] , 1.00000), 0.930000 , equal(constants[13] , 1.00000), 0.790000 , equal(constants[14] , 1.00000), 0.560000 , equal(constants[15] , 1.00000), 0.280000 , True, 1.00000])
    constants[69] = 1.00000
    constants[70] = custom_piecewise([equal(constants[10] , 1.00000), 0.770000 , equal(constants[11] , 1.00000), 0.500000 , True, 1.00000])
    constants[71] = 1000.00*(((-constants[20]*constants[21])/(constants[22]*constants[33]))*log((power(1.00000+constants[24]/2.60000, 4.00000))/(constants[32]*(power(1.00000+constants[24]/0.580000, 4.00000))))-0.0190000)
    constants[72] = custom_piecewise([equal(constants[16] , 1.00000), 0.700000 , equal(constants[17] , 1.00000), 0.500000 , equal(constants[18] , 1.00000), 0.300000 , equal(constants[19] , 1.00000), 0.100000 , True, 1.00000])
    
    # Buffer constants
    
    # SR-bound buffer
    constants[73] = 0.1e6                            # k_on_sr
    constants[74] = 0.06 * 1000                      # k_off_sr
    constants[75] = 20 / 1000                        # B_sr concentration in the cytosol
    states[18] = states[2]*constants[75]/(states[2] + constants[74]/constants[73])                             # initial SR concentration
    
    # CAM 
    constants[76] = 0.035e6                          # k_on_cam
    constants[77] = 0.2 * 1000                       # k_off_cam
    constants[78] = 24 / 1000                        # B_cam concentration in the cytosol
    states[19] = states[2]*constants[78]/(states[2] + constants[77]/constants[76])                            # initial cam concentration
    
    # SLH
    constants[79] = 0.1e6                            # k_on_slh
    constants[80] = 0.03 * 1000                      # k_off_slh
    constants[81] = 15 / 1000                        # B_sh concentration in the cytosol
    states[20] = states[2]*constants[81]/(states[2] + constants[80]/constants[79])                              # initial slh concentration
    
    # TnC
    constants[82] = 0.0327e6                         # k_on_tnc
    constants[83] = 19.6                             # k_off_tnc 
    constants[84] = 70 / 1000                        # B_TnC concentration in the cytosol
    states[21] = states[2]*constants[84]/(states[2] + constants[83]/constants[82])                         # initial TnC concentration
        
    # Rhod-2
    constants[85] = 0.1e6                            # k_on_rhod2 (mM-1 s-1)
    constants[86] = 0.15 * 1000                      # k_off_rhod2 (1/s)
    constants[87] = 20 / 1000                        # B_rhod2 concentration in the cytosol (mM)
    states[22] = states[2]*constants[87]/(states[2] + constants[86]/constants[85]) 
    
    # RyR constants
    constants[88] = 0.01                             # k_io and k_ic in 1/ms
    constants[89] = 1                                # Ci in muM
    constants[90] = 0.1                              # k_oc and k_i1i2 in 1/ms
    constants[91] = 3                                # k_a in 1/ms
    constants[92] = 17                               # g_rel in 1/s

    states[23] = 1.0                                 # initial probability of C
    states[24] = 0.0                                 # initial probability of R1
    states[25] = 0.0                                 # initial probability of R2
    states[26] = 0.0                                 # initial probability of O
    
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[5] = 0.330000+0.670000/(1.00000+exp((states[0]*1000.00+35.0000)/4.00000))
    algebraic[20] = ((600.000*exp(-(power(states[0]*1000.00+25.0000, 2.00000))/170.000)+(31.0000/(1.00000+exp((25.0000-states[0]*1000.00)/10.0000))+16.0000/(1.00000+exp((30.0000+states[0]*1000.00)/10.0000))))*constants[69])/1000.00
    rates[8] = (algebraic[5]-states[8])/algebraic[20]
    algebraic[11] = 1.00000/(1.00000+exp((states[0]*1000.00+77.8500)/5.00000))
    algebraic[26] = (1900.00/(1.00000+exp((states[0]*1000.00+15.0000)/10.0000)))/1000.00
    rates[13] = (algebraic[11]-states[13])/algebraic[26]
    algebraic[12] = 1.00000/(1.00000+exp((states[0]*1000.00+53.0000)/13.0000))
    algebraic[27] = (6.06000+39.1020/(0.570000*exp(-0.0800000*(states[0]*1000.00+44.0000))+0.0650000*exp(0.100000*(states[0]*1000.00+45.9300))))/1000.00
    rates[14] = (algebraic[12]-states[14])/algebraic[27]
    algebraic[13] = 1.00000/(1.00000+exp(-(states[0]*1000.00-22.3000)/18.7500))
    algebraic[28] = (2.75352+14.4052/(1.03700*exp(0.0900000*(states[0]*1000.00+30.6100))+0.369000*exp(-0.120000*(states[0]*1000.00+23.8400))))/1000.00
    rates[15] = (algebraic[13]-states[15])/algebraic[28]
    algebraic[14] = custom_piecewise([less_equal(states[2] , 0.000350000), 1.00000/(1.00000+power(states[2]/0.000350000, 6.00000)) , True, 1.00000/(1.00000+power(states[2]/0.000350000, 16.0000))])
    algebraic[29] = custom_piecewise([greater(algebraic[14] , states[17]) & greater(states[0] , -0.0600000), 0.00000 , True, 1.00000])
    rates[17] = (algebraic[29]*(algebraic[14]-states[17]))/constants[57]
    algebraic[4] = 1.00000/(1.00000+exp((states[0]*1000.00+26.0000)/3.00000))
    algebraic[19] = custom_piecewise([greater(algebraic[4]-states[7] , 0.00000), 1.00000+1433.00*(states[2]-50.0000*1.00000e-06) , True, 1.00000])
    algebraic[34] = ((20.0000+(1102.50*exp(-(power((power(states[0]*1000.00+27.0000, 2.00000))/15.0000, 2.00000)))+(200.000/(1.00000+exp((13.0000-states[0]*1000.00)/10.0000))+180.000/(1.00000+exp((30.0000+states[0]*1000.00)/10.0000)))))*algebraic[19])/1000.00
    rates[7] = (algebraic[4]-states[7])/algebraic[34]
    algebraic[0] = 1.00000/(power(1.00000+exp((-states[0]*1000.00-34.1000)/5.90000), 1.00000/3.00000))
    algebraic[15] = 1.00000/(1.00000+exp((-states[0]*1000.00-60.0000)/5.00000))
    algebraic[30] = 0.100000/(1.00000+exp((states[0]*1000.00+35.0000)/5.00000))+0.100000/(1.00000+exp((states[0]*1000.00-50.0000)/200.000))
    algebraic[40] = (1.00000*(algebraic[15]*algebraic[30]))/1000.00
    rates[3] = (algebraic[0]-states[3])/algebraic[40]
    algebraic[1] = 1.00000/(power(1.00000+exp((states[0]*1000.00+72.1000)/5.70000), 1.0/2))
    algebraic[16] = custom_piecewise([less(states[0] , -0.0400000), 0.0570000*exp(-(states[0]*1000.00+80.0000)/6.80000) , True, 0.00000])
    algebraic[31] = custom_piecewise([less(states[0] , -0.0400000), 2.70000*exp(0.0790000*(states[0]*1000.00))+3.10000*((power(10.0000, 5.00000))*exp(0.348500*(states[0]*1000.00))) , True, 0.770000/(0.130000*(1.00000+exp((states[0]*1000.00+10.6600)/-11.1000)))])
    algebraic[41] = custom_piecewise([less(states[0] , -0.0400000), 1.50000/((algebraic[16]+algebraic[31])*1000.00) , True, 2.54200/1000.00])
    rates[4] = (algebraic[1]-states[4])/algebraic[41]
    algebraic[2] = 1.00000/(power(1.00000+exp((states[0]*1000.00+72.1000)/5.70000), 1.0/2))
    algebraic[17] = custom_piecewise([less(states[0] , -0.0400000), ((-25428.0*exp(0.244400*(states[0]*1000.00))-6.94800*((power(10.0000, -6.00000))*exp(-0.0439100*(states[0]*1000.00))))*(states[0]*1000.00+37.7800))/(1.00000+exp(0.311000*(states[0]*1000.00+79.2300))) , True, 0.00000])
    algebraic[32] = custom_piecewise([less(states[0] , -0.0400000), (0.0242400*exp(-0.0105200*(states[0]*1000.00)))/(1.00000+exp(-0.137800*(states[0]*1000.00+40.1400))) , True, (0.600000*exp(0.0570000*(states[0]*1000.00)))/(1.00000+exp(-0.100000*(states[0]*1000.00+32.0000)))])
    algebraic[42] = 7.00000/((algebraic[17]+algebraic[32])*1000.00)
    rates[5] = (algebraic[2]-states[5])/algebraic[42]
    algebraic[7] = 1.00000/(1.00000+exp((constants[71]-states[0]*1000.00)/4.90000))
    algebraic[22] = 450.000/(1.00000+exp((-45.0000-states[0]*1000.00)/10.0000))
    algebraic[36] = 6.00000/(1.00000+exp((30.0000+states[0]*1000.00)/11.5000))
    algebraic[45] = (1.00000*(algebraic[22]*algebraic[36]))/1000.00
    rates[10] = (algebraic[7]-states[10])/algebraic[45]
    algebraic[8] = 1.00000/(1.00000+exp((states[0]*1000.00+88.0000)/50.0000))
    algebraic[23] = 3.00000/(1.00000+exp((-60.0000-states[0]*1000.00)/20.0000))
    algebraic[37] = 1.12000/(1.00000+exp((-60.0000+states[0]*1000.00)/20.0000))
    algebraic[46] = (1.00000*(algebraic[23]*algebraic[37]))/1000.00
    rates[11] = (algebraic[8]-states[11])/algebraic[46]
    algebraic[9] = 1.00000/(1.00000+exp((-states[0]*1000.00-20.0000)/16.0000))
    algebraic[24] = 1100.00/(power(1.00000+exp((-10.0000-states[0]*1000.00)/6.00000), 1.0/2))
    algebraic[38] = 1.00000/(1.00000+exp((-60.0000+states[0]*1000.00)/20.0000))
    algebraic[47] = (1.00000*(algebraic[24]*algebraic[38]))/1000.00
    rates[12] = (algebraic[9]-states[12])/algebraic[47]
    algebraic[3] = 1.00000/(1.00000+exp(-(states[0]*1000.00+9.10000)/7.00000))
    algebraic[18] = 0.250000+1.40000/(1.00000+exp((-states[0]*1000.00-35.0000)/13.0000))
    algebraic[33] = 1.40000/(1.00000+exp((states[0]*1000.00+5.00000)/5.00000))
    algebraic[43] = 1.00000/(1.00000+exp((-states[0]*1000.00+50.0000)/20.0000))
    algebraic[49] = ((algebraic[18]*algebraic[33]+algebraic[43])*1.00000)/1000.00
    rates[6] = (algebraic[3]-states[6])/algebraic[49]
    algebraic[6] = 1.00000/(1.00000+power(states[2]/0.000600000, 8.00000))
    algebraic[21] = 0.100000/(1.00000+exp((states[2]-0.000900000)/0.000100000))
    algebraic[35] = 0.300000/(1.00000+exp((states[2]-0.000750000)/0.000800000))
    algebraic[44] = (algebraic[6]+(algebraic[21]+algebraic[35]))/1.31560
    algebraic[50] = custom_piecewise([greater(states[0] , -0.0600000) & greater(algebraic[44] , states[9]), 0.00000 , True, 1.00000])
    rates[9] = (algebraic[50]*(algebraic[44]-states[9]))/constants[30]
    algebraic[25] = ((constants[20]*constants[21])/constants[22])*log(constants[23]/states[1])
    algebraic[51] = constants[67]*(constants[28]*((power(states[3], 3.00000))*(states[4]*(states[5]*(states[0]-algebraic[25])))))
    algebraic[62] = ((((constants[42]*constants[26])/(constants[26]+constants[40]))*states[1])/(states[1]+constants[41]))/(1.00000+(0.124500*exp((-0.100000*(states[0]*constants[22]))/(constants[20]*constants[21]))+0.0353000*exp((-states[0]*constants[22])/(constants[20]*constants[21]))))
    algebraic[63] = (constants[43]*(exp((constants[45]*(states[0]*constants[22]))/(constants[20]*constants[21]))*((power(states[1], 3.00000))*constants[24])-exp(((constants[45]-1.00000)*(states[0]*constants[22]))/(constants[20]*constants[21]))*((power(constants[23], 3.00000))*(states[2]*constants[44]))))/((power(constants[48], 3.00000)+power(constants[23], 3.00000))*((constants[47]+constants[24])*(1.00000+constants[46]*exp(((constants[45]-1.00000)*(states[0]*constants[22]))/(constants[20]*constants[21])))))
    algebraic[60] = constants[38]*(states[0]-algebraic[25])
    rates[1] = (-constants[0]*(algebraic[51]+(algebraic[60]+(3.00000*algebraic[62]+3.00000*algebraic[63]))))/(constants[22]*(constants[52]*1.00000e-18))
    algebraic[52] = ((((constants[29]*(4.00000*(states[0]*(power(constants[22], 2.00000)))))/(constants[20]*constants[21]))*(states[2]*exp((2.00000*(states[0]*constants[22]))/(constants[20]*constants[21]))-0.341000*constants[24]))/(exp((2.00000*(states[0]*constants[22]))/(constants[20]*constants[21]))-1.00000))*(states[6]*(states[7]*(states[8]*states[9])))
    algebraic[55] = 3.91000/(1.00000+exp(0.594200*((states[0]*1000.00-constants[66]*1000.00)-200.000)))
    algebraic[56] = (-1.50900*exp(0.000200000*((states[0]*1000.00-constants[66]*1000.00)+100.000))+exp(0.588600*((states[0]*1000.00-constants[66]*1000.00)-10.0000)))/(1.00000+exp(0.454700*(states[0]*1000.00-constants[66]*1000.00)))
    algebraic[57] = algebraic[55]/(algebraic[55]+algebraic[56])
    algebraic[58] = constants[35]*(algebraic[57]*((states[0]-constants[66])*(power(constants[26]/5.40000, 1.0/2))))
    algebraic[59] = constants[36]*(states[13]*(states[0]-constants[37]))
    algebraic[53] = constants[70]*(constants[31]*((states[0]-constants[66])*(states[10]*(states[11]*(power(constants[26]/5.40000, 1.0/2))))))
    algebraic[39] = ((constants[20]*constants[21])/constants[22])*log((constants[26]+constants[27]*constants[23])/(constants[25]+constants[27]*states[1]))
    algebraic[54] = constants[72]*(constants[34]*((states[0]-algebraic[39])*((power(states[12], 2.00000))*(1.00000+0.600000/(1.00000+power((3.80000*1.00000e-05)/states[2], 1.40000))))))
    algebraic[65] = constants[51]*((states[0]-constants[66])*(states[14]*states[15]))
    algebraic[64] = (constants[49]*states[2])/(states[2]+constants[50])
    algebraic[48] = ((0.500000*(constants[20]*constants[21]))/constants[22])*log(constants[24]/states[2])
    algebraic[61] = constants[39]*(states[0]-algebraic[48])
    
    # Stimulating current
    algebraic[10] = custom_piecewise([greater_equal(voi , constants[2]) & (less_equal(voi , constants[3]) & less_equal((voi-constants[2])-floor((voi-constants[2])/constants[65])*constants[65] , constants[6])), (constants[1]*constants[4])/constants[0] , True, 0.00000])
    
    rates[0] = -((algebraic[58]+(algebraic[65]+(algebraic[53]+(algebraic[54]+(algebraic[52]+(algebraic[62]+(algebraic[51]+(algebraic[63]+(algebraic[64]+(algebraic[59]+(algebraic[60]+algebraic[61])))))))))))-algebraic[10])
    algebraic[69] = 1.00000/(1.00000+(constants[59]*constants[61])/(power(states[2]+constants[61], 2.00000)))
    algebraic[67] = constants[63]/(1.00000+(power(constants[58], 2.00000))/(power(states[2], 2.00000)))
    algebraic[68] = (states[16]-states[2])*constants[64]
    algebraic[70] = 1.00000/(1.00000+(constants[60]*constants[62])/(power(states[16]+constants[62], 2.00000)))

    
    # Modification of the buffer in d/dt Ca_i without the rapid buffer approximation
    Ca = states[2]
    
    # SR buffer
    SR = states[18]
    k_on_sr = constants[73]
    k_off_sr = constants[74]
    B_SR = constants[75]
    
    rates[18] = k_on_sr * Ca * (B_SR - SR) - k_off_sr * SR
    
    # CAM 
    CAM = states[19]
    k_on_cam = constants[76]
    k_off_cam = constants[77]
    B_CAM = constants[78]
    
    rates[19] = k_on_cam * Ca * (B_CAM - CAM) - k_off_cam * CAM
    
    # SLH 
    SLH = states[20]
    k_on_slh = constants[79]
    k_off_slh = constants[80]
    B_SLH = constants[81]
    
    rates[20] = k_on_slh * Ca * (B_SLH - SLH) - k_off_slh * SLH
    
    # TnC
    TnC = states[21]
    k_on_tnc = constants[82]
    k_off_tnc = constants[83]
    B_TnC = constants[84]
    
    rates[21] = k_on_tnc * Ca * (B_TnC - TnC) - k_off_tnc * TnC
    
    # Rhod-2
    RD2 = states[22]
    k_on_Rhod2 = constants[85]
    k_off_Rhod2 = constants[86]
    B_Rhod2 = constants[87]
    
    rates[22] = k_on_Rhod2 * Ca * (B_Rhod2- RD2) - k_off_Rhod2 * RD2
    #Rhod-2 buffer turned off
    rates[22] = 0

    
    Buffer = rates[18] + rates[19] + rates[20] + rates[21] + rates[22] 
    
    # RnR 
    Ca = states[2] * 1000       # in muM
    k_oc = constants[90]        # in 1/ms
    k_i1i2 = k_oc
    k_io = constants[88]        # in 1/ms
    k_ic = k_io
    Ca_SR = states[16] * 1000   # in muM
    f2 = 1 + (200/Ca_SR)**2
    k_oi = 10**-2 * (Ca) * f2
    k_ci = k_oi
    Ci = constants[89]          # in muM
    k_a = constants[91]         # in 1/ms
    k_CaSR = (1 + (80 / Ca_SR)**25) / (1 + (Ca_SR / 120)**10)
    
    k_co =  k_a * ((Ca/Ci)**3/(1 + (Ca/Ci)**3)) / k_CaSR
    k_i2i1 = k_co
    
    O = states[26]
    C = states[23]
    R1 = states[24]
    R2 = states[25]

    
    # dO/dt
    rates[26] = (k_co * C + k_io * R1 - (k_oc + k_oi) * O) * 1000          # in 1/s
    # dC/dt
    rates[23] = (k_oc * O + k_ic * R2 - (k_co + k_ci) * C) * 1000          # in 1/s
    # dR1/dt
    rates[24] = (k_oi * C + k_i2i1 * R2 - (k_i1i2 + k_io) * R1) * 1000     # in 1/s
    # dR2/dt 
    rates[25] =  - (rates[26] + rates[23] + rates[24])                     # in 1/s
    
    # I_rel 
    g_rel = constants[92]
    algebraic[66] = g_rel * O * (states[16] - states[2])
    
    # Free Ca dynamics
    rates[2] = (((algebraic[68]-algebraic[67])+algebraic[66])-(((algebraic[52]+(algebraic[61]+algebraic[64]))-2.00000*algebraic[63])*constants[0])/(2.00000*(constants[52]*(constants[22]*1.00000e-18)))) - Buffer
    # Ca_SR dynamics
    rates[16] = ((algebraic[70]*constants[52])/constants[53])*(algebraic[67]-(algebraic[66]+algebraic[68]))
    
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[5] = 0.330000+0.670000/(1.00000+exp((states[0]*1000.00+35.0000)/4.00000))
    algebraic[20] = ((600.000*exp(-(power(states[0]*1000.00+25.0000, 2.00000))/170.000)+(31.0000/(1.00000+exp((25.0000-states[0]*1000.00)/10.0000))+16.0000/(1.00000+exp((30.0000+states[0]*1000.00)/10.0000))))*constants[69])/1000.00
    algebraic[11] = 1.00000/(1.00000+exp((states[0]*1000.00+77.8500)/5.00000))
    algebraic[26] = (1900.00/(1.00000+exp((states[0]*1000.00+15.0000)/10.0000)))/1000.00
    algebraic[12] = 1.00000/(1.00000+exp((states[0]*1000.00+53.0000)/13.0000))
    algebraic[27] = (6.06000+39.1020/(0.570000*exp(-0.0800000*(states[0]*1000.00+44.0000))+0.0650000*exp(0.100000*(states[0]*1000.00+45.9300))))/1000.00
    algebraic[13] = 1.00000/(1.00000+exp(-(states[0]*1000.00-22.3000)/18.7500))
    algebraic[28] = (2.75352+14.4052/(1.03700*exp(0.0900000*(states[0]*1000.00+30.6100))+0.369000*exp(-0.120000*(states[0]*1000.00+23.8400))))/1000.00
    algebraic[14] = custom_piecewise([less_equal(states[2] , 0.000350000), 1.00000/(1.00000+power(states[2]/0.000350000, 6.00000)) , True, 1.00000/(1.00000+power(states[2]/0.000350000, 16.0000))])
    algebraic[29] = custom_piecewise([greater(algebraic[14] , states[17]) & greater(states[0] , -0.0600000), 0.00000 , True, 1.00000])
    algebraic[4] = 1.00000/(1.00000+exp((states[0]*1000.00+26.0000)/3.00000))
    algebraic[19] = custom_piecewise([greater(algebraic[4]-states[7] , 0.00000), 1.00000+1433.00*(states[2]-50.0000*1.00000e-06) , True, 1.00000])
    algebraic[34] = ((20.0000+(1102.50*exp(-(power((power(states[0]*1000.00+27.0000, 2.00000))/15.0000, 2.00000)))+(200.000/(1.00000+exp((13.0000-states[0]*1000.00)/10.0000))+180.000/(1.00000+exp((30.0000+states[0]*1000.00)/10.0000)))))*algebraic[19])/1000.00
    algebraic[0] = 1.00000/(power(1.00000+exp((-states[0]*1000.00-34.1000)/5.90000), 1.00000/3.00000))
    algebraic[15] = 1.00000/(1.00000+exp((-states[0]*1000.00-60.0000)/5.00000))
    algebraic[30] = 0.100000/(1.00000+exp((states[0]*1000.00+35.0000)/5.00000))+0.100000/(1.00000+exp((states[0]*1000.00-50.0000)/200.000))
    algebraic[40] = (1.00000*(algebraic[15]*algebraic[30]))/1000.00
    algebraic[1] = 1.00000/(power(1.00000+exp((states[0]*1000.00+72.1000)/5.70000), 1.0/2))
    algebraic[16] = custom_piecewise([less(states[0] , -0.0400000), 0.0570000*exp(-(states[0]*1000.00+80.0000)/6.80000) , True, 0.00000])
    algebraic[31] = custom_piecewise([less(states[0] , -0.0400000), 2.70000*exp(0.0790000*(states[0]*1000.00))+3.10000*((power(10.0000, 5.00000))*exp(0.348500*(states[0]*1000.00))) , True, 0.770000/(0.130000*(1.00000+exp((states[0]*1000.00+10.6600)/-11.1000)))])
    algebraic[41] = custom_piecewise([less(states[0] , -0.0400000), 1.50000/((algebraic[16]+algebraic[31])*1000.00) , True, 2.54200/1000.00])
    algebraic[2] = 1.00000/(power(1.00000+exp((states[0]*1000.00+72.1000)/5.70000), 1.0/2))
    algebraic[17] = custom_piecewise([less(states[0] , -0.0400000), ((-25428.0*exp(0.244400*(states[0]*1000.00))-6.94800*((power(10.0000, -6.00000))*exp(-0.0439100*(states[0]*1000.00))))*(states[0]*1000.00+37.7800))/(1.00000+exp(0.311000*(states[0]*1000.00+79.2300))) , True, 0.00000])
    algebraic[32] = custom_piecewise([less(states[0] , -0.0400000), (0.0242400*exp(-0.0105200*(states[0]*1000.00)))/(1.00000+exp(-0.137800*(states[0]*1000.00+40.1400))) , True, (0.600000*exp(0.0570000*(states[0]*1000.00)))/(1.00000+exp(-0.100000*(states[0]*1000.00+32.0000)))])
    algebraic[42] = 7.00000/((algebraic[17]+algebraic[32])*1000.00)
    algebraic[7] = 1.00000/(1.00000+exp((constants[71]-states[0]*1000.00)/4.90000))
    algebraic[22] = 450.000/(1.00000+exp((-45.0000-states[0]*1000.00)/10.0000))
    algebraic[36] = 6.00000/(1.00000+exp((30.0000+states[0]*1000.00)/11.5000))
    algebraic[45] = (1.00000*(algebraic[22]*algebraic[36]))/1000.00
    algebraic[8] = 1.00000/(1.00000+exp((states[0]*1000.00+88.0000)/50.0000))
    algebraic[23] = 3.00000/(1.00000+exp((-60.0000-states[0]*1000.00)/20.0000))
    algebraic[37] = 1.12000/(1.00000+exp((-60.0000+states[0]*1000.00)/20.0000))
    algebraic[46] = (1.00000*(algebraic[23]*algebraic[37]))/1000.00
    algebraic[9] = 1.00000/(1.00000+exp((-states[0]*1000.00-20.0000)/16.0000))
    algebraic[24] = 1100.00/(power(1.00000+exp((-10.0000-states[0]*1000.00)/6.00000), 1.0/2))
    algebraic[38] = 1.00000/(1.00000+exp((-60.0000+states[0]*1000.00)/20.0000))
    algebraic[47] = (1.00000*(algebraic[24]*algebraic[38]))/1000.00
    algebraic[3] = 1.00000/(1.00000+exp(-(states[0]*1000.00+9.10000)/7.00000))
    algebraic[18] = 0.250000+1.40000/(1.00000+exp((-states[0]*1000.00-35.0000)/13.0000))
    algebraic[33] = 1.40000/(1.00000+exp((states[0]*1000.00+5.00000)/5.00000))
    algebraic[43] = 1.00000/(1.00000+exp((-states[0]*1000.00+50.0000)/20.0000))
    algebraic[49] = ((algebraic[18]*algebraic[33]+algebraic[43])*1.00000)/1000.00
    algebraic[6] = 1.00000/(1.00000+power(states[2]/0.000600000, 8.00000))
    algebraic[21] = 0.100000/(1.00000+exp((states[2]-0.000900000)/0.000100000))
    algebraic[35] = 0.300000/(1.00000+exp((states[2]-0.000750000)/0.000800000))
    algebraic[44] = (algebraic[6]+(algebraic[21]+algebraic[35]))/1.31560
    algebraic[50] = custom_piecewise([greater(states[0] , -0.0600000) & greater(algebraic[44] , states[9]), 0.00000 , True, 1.00000])
    algebraic[25] = ((constants[20]*constants[21])/constants[22])*log(constants[23]/states[1])
    algebraic[51] = constants[67]*(constants[28]*((power(states[3], 3.00000))*(states[4]*(states[5]*(states[0]-algebraic[25])))))
    algebraic[62] = ((((constants[42]*constants[26])/(constants[26]+constants[40]))*states[1])/(states[1]+constants[41]))/(1.00000+(0.124500*exp((-0.100000*(states[0]*constants[22]))/(constants[20]*constants[21]))+0.0353000*exp((-states[0]*constants[22])/(constants[20]*constants[21]))))
    algebraic[63] = (constants[43]*(exp((constants[45]*(states[0]*constants[22]))/(constants[20]*constants[21]))*((power(states[1], 3.00000))*constants[24])-exp(((constants[45]-1.00000)*(states[0]*constants[22]))/(constants[20]*constants[21]))*((power(constants[23], 3.00000))*(states[2]*constants[44]))))/((power(constants[48], 3.00000)+power(constants[23], 3.00000))*((constants[47]+constants[24])*(1.00000+constants[46]*exp(((constants[45]-1.00000)*(states[0]*constants[22]))/(constants[20]*constants[21])))))
    algebraic[60] = constants[38]*(states[0]-algebraic[25])
    algebraic[52] = ((((constants[29]*(4.00000*(states[0]*(power(constants[22], 2.00000)))))/(constants[20]*constants[21]))*(states[2]*exp((2.00000*(states[0]*constants[22]))/(constants[20]*constants[21]))-0.341000*constants[24]))/(exp((2.00000*(states[0]*constants[22]))/(constants[20]*constants[21]))-1.00000))*(states[6]*(states[7]*(states[8]*states[9])))
    algebraic[55] = 3.91000/(1.00000+exp(0.594200*((states[0]*1000.00-constants[66]*1000.00)-200.000)))
    algebraic[56] = (-1.50900*exp(0.000200000*((states[0]*1000.00-constants[66]*1000.00)+100.000))+exp(0.588600*((states[0]*1000.00-constants[66]*1000.00)-10.0000)))/(1.00000+exp(0.454700*(states[0]*1000.00-constants[66]*1000.00)))
    algebraic[57] = algebraic[55]/(algebraic[55]+algebraic[56])
    algebraic[58] = constants[35]*(algebraic[57]*((states[0]-constants[66])*(power(constants[26]/5.40000, 1.0/2))))
    algebraic[59] = constants[36]*(states[13]*(states[0]-constants[37]))
    algebraic[53] = constants[70]*(constants[31]*((states[0]-constants[66])*(states[10]*(states[11]*(power(constants[26]/5.40000, 1.0/2))))))
    algebraic[39] = ((constants[20]*constants[21])/constants[22])*log((constants[26]+constants[27]*constants[23])/(constants[25]+constants[27]*states[1]))
    algebraic[54] = constants[72]*(constants[34]*((states[0]-algebraic[39])*((power(states[12], 2.00000))*(1.00000+0.600000/(1.00000+power((3.80000*1.00000e-05)/states[2], 1.40000))))))
    algebraic[65] = constants[51]*((states[0]-constants[66])*(states[14]*states[15]))
    algebraic[64] = (constants[49]*states[2])/(states[2]+constants[50])
    algebraic[48] = ((0.500000*(constants[20]*constants[21]))/constants[22])*log(constants[24]/states[2])
    algebraic[61] = constants[39]*(states[0]-algebraic[48])
    algebraic[10] = custom_piecewise([greater_equal(voi , constants[2]) & (less_equal(voi , constants[3]) & less_equal((voi-constants[2])-floor((voi-constants[2])/constants[65])*constants[65] , constants[6])), (constants[1]*constants[4])/constants[0] , True, 0.00000])
    algebraic[69] = 1.00000/(1.00000+(constants[59]*constants[61])/(power(states[2]+constants[61], 2.00000)))
    algebraic[66] = constants[92] * states[22] * (states[16] - states[2])
    algebraic[67] = constants[63]/(1.00000+(power(constants[58], 2.00000))/(power(states[2], 2.00000)))
    algebraic[68] = (states[16]-states[2])*constants[64]*0
    algebraic[70] = 1.00000/(1.00000+(constants[60]*constants[62])/(power(states[16]+constants[62], 2.00000)))
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model(tf = 5):
    """Solve model with ODE solver"""
    from scipy.integrate import ode, solve_ivp
    # Initialise constants and state variables
    
        
    (init_states, constants) = initConsts()

    # Set intial integration time
    t0 = 0

    sol = solve_ivp(computeRates, [t0, tf], init_states, method = 'BDF',  atol=1e-06, rtol=1e-06, args = [constants], max_step = 0.001)
    voi = sol.t
    states = sol.y

    
    # Turn states string into array with the appropiate shape
    states = array(states)
    
    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)


def plot_model(voi, y):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,y)
    pylab.xlabel(legend_voi)
    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()

if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
    plot_model(voi, states[0])
    