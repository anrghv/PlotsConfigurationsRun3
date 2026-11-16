#ifndef HGG_BDT_HEADERS_H
#define HGG_BDT_HEADERS_H

#include <TMVA/RBDT.hxx>
#include <vector>

// Single-model evaluation.
// Argument order MUST match mvaVariables in xgb_train.py exactly (32 features).
inline float eval_xgboost(
    float Lepton_pt0, float Lepton_pt1, float ptll, float mll,
    float PuppiMET_pt,
    float LowestQGLJet_pt1, float LowestQGLJet_pt2, float LowestQGLJet_pt3,
    float LowestQGLJet_eta1, float LowestQGLJet_eta2,
    float LowestQGLJet_phi1, float LowestQGLJet_phi2,
    float LowestQGLJet_mass1, float LowestQGLJet_mass2,
    float qgl_j1_lowestqgl,
    float btagDeepBj1_lowestqgl, float btagDeepBj2_lowestqgl,
    float btagCSVV2j1_lowestqgl, float btagCSVV2j2_lowestqgl,
    float mjj, float mjj_qgl, float ptjj_qgl,
    float detajj, float detajj_qgl,
    float dphijj, float dphijj_qgl,
    float drjj, float drjj_qgl,
    float dphilljet, float dphilljet_qgl,
    float dphilljetjet, float dphilljetjet_qgl
) {
    // static: the model file is read from EOS only once per process
    static TMVA::Experimental::RBDT bdt(
        "bdt_model",   // must equal the key used in SaveXGBoost
        "/eos/user/a/araghav/xgboost/inputs_plot-config/xgb_Hgg_xgb_tuned_2.root"
    );

    std::vector<float> inputs = {
        Lepton_pt0, Lepton_pt1, ptll, mll,
        PuppiMET_pt,
        LowestQGLJet_pt1, LowestQGLJet_pt2, LowestQGLJet_pt3,
        LowestQGLJet_eta1, LowestQGLJet_eta2,
        LowestQGLJet_phi1, LowestQGLJet_phi2,
        LowestQGLJet_mass1, LowestQGLJet_mass2,
        qgl_j1_lowestqgl,
        btagDeepBj1_lowestqgl, btagDeepBj2_lowestqgl,
        btagCSVV2j1_lowestqgl, btagCSVV2j2_lowestqgl,
        mjj, mjj_qgl, ptjj_qgl,
        detajj, detajj_qgl,
        dphijj, dphijj_qgl,
        drjj, drjj_qgl,
        dphilljet, dphilljet_qgl,
        dphilljetjet, dphilljetjet_qgl
    };

    return bdt.Compute(inputs)[0];
}

#endif