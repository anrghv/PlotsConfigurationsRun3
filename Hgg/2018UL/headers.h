#ifndef HGG_BDT_HEADERS_H
#define HGG_BDT_HEADERS_H

#include <TMVA/RBDT.hxx>
#include <vector>

// Single-model evaluation.
inline float eval_xgboost(
    float Lepton_pt1,
    float ptll,
    float mll,
    float LowestQGLJet_pt1,
    float LowestQGLJet_mass1,
    float qgl_j1_lowestqgl,
    float mjj,
    float mjj_qgl,
    float detajj,
    float detajj_qgl,
    float drjj,
    float CleanJet_pt0,
    float CleanJet_pt1
) {
    // static: the model file is read from EOS only once per process
    static TMVA::Experimental::RBDT bdt(
        "bdt_model",   // must equal the key used in SaveXGBoost
        "/eos/user/a/araghav/xgboost/inputs_plot-config/xgb_Hgg_xgb_config_2.root"
    );

    std::vector<float> inputs = {
        Lepton_pt1,
        ptll,
        mll,
        LowestQGLJet_pt1,
        LowestQGLJet_mass1,
        qgl_j1_lowestqgl,
        mjj,
        mjj_qgl,
        detajj,
        detajj_qgl,
        drjj,
        CleanJet_pt0,
        CleanJet_pt1
    };

    return bdt.Compute(inputs)[0];
}

#endif