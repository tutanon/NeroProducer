#include "NeroProducer/Nero/interface/NeroTaus.hpp"
#include "NeroProducer/Nero/interface/Nero.hpp"

NeroTaus::NeroTaus(): 
        NeroCollection(),
        BareTaus()
{
    mMinPt = 18;
    mMinNtaus = 0;
    mMinEta = 2.3;
    mMinId = "decayModeFinding";
    mMaxIso = -1;
}

NeroTaus::~NeroTaus(){
}

int NeroTaus::analyze(const edm::Event & iEvent)
{
    if ( mOnlyMc  ) return 0;

    iEvent.getByToken(token, handle);
    if ( not handle.isValid() ) cout<<"[NeroTaus]::[analyze]::[ERROR] handle is not valid"<<endl;

    for (const pat::Tau &tau : *handle) {

        if (tau.pt() < 18 ) continue;	
        if (tau.pt() < mMinPt ) continue;	
        
        /// miniaod taus = decayModeFindingNewDMs
        if ( mMinId != "" and !(tau.tauID(mMinId)) ) continue; // minimum requirement to be saved.
        if ( mMaxIso >=0 and tau.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") >= mMaxIso ) continue;

        if ( fabs(tau.eta()) > mMinEta ) continue;
        
        // ------------ END SELECTION 

         float phoIso = 0.; for(auto cand : tau.isolationGammaCands() ) phoIso += cand->pt();//tau.isolationPFGammaCandsEtSum() ;
         float chIso  = 0.; for(auto cand : tau.isolationChargedHadrCands() ) chIso += cand->pt();//tau.isolationPFChargedHadrCandsPtSum();
         float nhIso  = 0.; for(auto cand : tau.isolationNeutrHadrCands() ) nhIso += cand->pt(); // PF Cands not exists in miniAOD
         float totIso = phoIso + chIso + nhIso;
        
        //FILL
        new ( (*p4)[p4->GetEntriesFast()]) TLorentzVector(tau.px(), tau.py(), tau.pz(), tau.energy());

        unsigned bits = 0;
        bits |= bool(tau.tauID("decayModeFindingNewDMs") ) * TauDecayModeFindingNewDMs;
        bits |= bool(tau.tauID("decayModeFinding") ) * TauDecayModeFinding;
        bits |= bool(tau.tauID("againstElectronLooseMVA5") )* AgainstEleLoose  ; // FIXME 76 MVA 6
        bits |= bool(tau.tauID("againstElectronMediumMVA5"))* AgainstEleMedium ;
        bits |= bool(tau.tauID("againstMuonLoose3"))        * AgainstMuLoose   ;
        bits |= bool(tau.tauID("againstMuonTight3"))        * AgainstMuTight   ;
        // old id the following only in 76 FIXME
        //bits |= bool(tau.tauID("byLooseIsolationMVArun2v1DBoldDMwLT")) * byLooseIsolationMVArun2v1DBoldDMwLT;
        //bits |= bool(tau.tauID("byMediumIsolationMVArun2v1DBoldDMwLT")) * byMediumIsolationMVArun2v1DBoldDMwLT;
        //bits |= bool(tau.tauID("byTightIsolationMVArun2v1DBoldDMwLT")) * byTightIsolationMVArun2v1DBoldDMwLT;
        //bits |= bool(tau.tauID("byVTightIsolationMVArun2v1DBoldDMwLT")) * byVTightIsolationMVArun2v1DBoldDMwLT;
        //// new id
        //bits |= bool(tau.tauID("byLooseIsolationMVArun2v1DBnewDMwLT")) * byLooseIsolationMVArun2v1DBnewDMwLT;
        //bits |= bool(tau.tauID("byMediumIsolationMVArun2v1DBnewDMwLT")) * byMediumIsolationMVArun2v1DBnewDMwLT;
        //bits |= bool(tau.tauID("byTightIsolationMVArun2v1DBnewDMwLT")) * byTightIsolationMVArun2v1DBnewDMwLT;
        //bits |= bool(tau.tauID("byVTightIsolationMVArun2v1DBnewDMwLT")) * byVTightIsolationMVArun2v1DBnewDMwLT;
        selBits -> push_back(bits);
        Q -> push_back( tau.charge() );
        M -> push_back( tau.mass() );
        iso -> push_back( totIso ) ; 

        if (IsExtend() ){
            chargedIsoPtSum  -> push_back( tau.tauID("chargedIsoPtSum") );
            neutralIsoPtSum  -> push_back( tau.tauID("neutralIsoPtSum") );
            isoDeltaBetaCorr -> push_back( tau.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits"));
            isoPileupWeightedRaw -> push_back( tau.tauID("byPileupWeightedIsolationRaw3Hits"));

        }


    }
    if( int(selBits->size()) < mMinNtaus) return 1;
    return 0;
}


// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
