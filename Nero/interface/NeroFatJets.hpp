#ifndef NERO_FATJETS_H
#define NERO_FATJETS_H

#include "NeroProducer/Nero/interface/NeroCollection.hpp"
#include "NeroProducer/Core/interface/BareFatJets.hpp"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"


class NeroFatJets : virtual public NeroCollection, 
    virtual public BareFatJets
{
    public:
        NeroFatJets();
        ~NeroFatJets();
        int analyze(const edm::Event& iEvent);
        virtual inline string name(){return "NeroFatJets";};
        void init() override;

        // --- specific fuctions
        // --- Handle
        edm::Handle<pat::JetCollection> handle;	
        edm::Handle<double> rho_handle;
        edm::Handle<reco::VertexCollection> vertex_handle;
    
        // --- Token
        edm::EDGetTokenT<pat::JetCollection> token;
        edm::EDGetTokenT<double> rho_token;
        edm::EDGetTokenT<reco::PFJetCollection> subjets_token;
        edm::EDGetTokenT<reco::JetTagCollection> btags_token;
        edm::EDGetTokenT<reco::VertexCollection> vertex_token;        

        // --- configuration
        float mMinPt;
        float mMaxEta;
        bool mRunJEC=false;
        string mMinId;
        float jetRadius; // used for subjet matching
        FactorizedJetCorrector *mMCJetCorrector;   // needed for reclustered jets
        FactorizedJetCorrector *mDataJetCorrector; 

};


#endif
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
