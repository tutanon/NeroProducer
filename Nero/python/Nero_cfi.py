import FWCore.ParameterSet.Config as cms

from subprocess import check_output
import os

#------------------------------------------------------
nero = cms.EDAnalyzer("Nero",
    info = cms.string("Nero"),
    cmssw = cms.string( os.environ['CMSSW_VERSION'] ) , # no need to ship it with the grid option
    head = cms.string( check_output("cd "+os.environ['CMSSW_BASE']+"/src/NeroProducer/ && git rev-parse HEAD && cd - 2>&1 >/dev/null",shell=True) ) ,
    tag  = cms.string( check_output("cd " +os.environ["CMSSW_BASE"] +"/src/NeroProducer && { git describe --tags || true ; } && cd - 2>&1 >/dev/null",shell=True) ) ,

    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    muons = cms.InputTag("slimmedMuons"),
    electrons = cms.InputTag("slimmedElectrons"),
    taus = cms.InputTag("slimmedTaus"),
    photons = cms.InputTag("slimmedPhotons"),
    jets = cms.InputTag("slimmedJets"),
    puppijets = cms.InputTag("slimmedJetsPuppi"),

    ############### RECLUSTERED JETS and MET

    doReclustering = cms.bool(False),
    chsAK8 = cms.InputTag("slimmedJetsAK8"),
    puppiAK8 = cms.InputTag("packedPatJetsPFAK8Puppi"),
    chsCA15 = cms.InputTag("packedPatJetsPFCA15CHS"),
    puppiCA15 = cms.InputTag("packedPatJetsPFCA15Puppi"),

    mets = cms.InputTag("slimmedMETs"),
    metsPuppi = cms.InputTag("slimmedMETsPuppi"),
    #metsPuppi = cms.InputTag("type1PuppiMET"),  ## RECLUSTERING
    #metsPuppiUncorrected = cms.InputTag("pfMETPuppi"), ## RECLUSTERING
    pfCands = cms.InputTag("packedPFCandidates"),


    # gen
    pileup = cms.InputTag("slimmedAddPileupInfo"),
    generator = cms.InputTag("generator"),
    genruninfo = cms.InputTag("generator"),
    lhe = cms.InputTag("externalLHEProducer"),
    genjets = cms.InputTag("slimmedGenJets"),
    prunedgen = cms.InputTag("prunedGenParticles"),
    packedgen = cms.InputTag("packedGenParticles"),
    ### ID MAP, these will become input tag when replacing the %(bx)s field, see testNero.py
    eleVetoIdMap   = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-%(bx)s-%(vs)s-standalone-veto"),
    eleLooseIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-%(bx)s-%(vs)s-standalone-loose"),
    eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-%(bx)s-%(vs)s-standalone-medium"),
    eleTightIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-%(bx)s-%(vs)s-standalone-tight"),
    eleMvaMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
    phoLooseIdMap  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-%(bx)s-%(vs)s-standalone-loose"),
    phoMediumIdMap = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-%(bx)s-%(vs)s-standalone-medium"),
    phoTightIdMap  = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-%(bx)s-%(vs)s-standalone-tight"),
    ### ISO MAP
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer:phoChargedIsolation"),
    phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer:phoNeutralHadronIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer:phoPhotonIsolation"),

    ## MET Filters
    metfilterNames = cms.vstring(['Flag_HBHENoiseFilter', 
                                  'Flag_HBHENoiseIsoFilter', 
                                  'Flag_CSCTightHalo2015Filter', 
                                  'Flag_EcalDeadCellTriggerPrimitiveFilter', 
                                  'Flag_goodVertices', 
                                  'Flag_eeBadScFilter',
                                  'Flag_globalTightHalo2016Filter'
                                  ]),
    metFilterToken = cms.InputTag("TriggerResults","","RECO"),          

    #
    ## TRIGGER
    triggerNames = cms.vstring([
                                'HLT_Ele23_WPLoose_Gsf_v',
                                'HLT_Ele27_WPLoose_Gsf_v',
                                'HLT_IsoMu24_v',
                                'HLT_Mu50_v',
                                'HLT_PFMET170_HBHECleaned_v',
                                'HLT_PFMET170_JetIdCleaned_v',
                                'HLT_PFMET170_NoiseCleaned_v',
                                'HLT_PFMET170_NotCleaned_v',
                                'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v',
                                'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v',
                                'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v',
                                'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
                                'HLT_Photon165_HE10_v',
                                'HLT_Photon120_R9Id90_HE10_IsoM_v',
                                ##Guillelmo
                                'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v',
                                'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v',
                                'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v',
                                'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',
                                'HLT_IsoMu18_v',
                                'HLT_IsoTkMu18_v',
                                'HLT_IsoTkMu24_v',
                                'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
                                'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
                                'HLT_Ele22_eta2p1_WPLoose_Gsf_v',
                                'HLT_Mu8_TrkIsoVVL_v',
                                'HLT_Mu17_TrkIsoVVL_v',
                                'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v',
                                'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v',
                                'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_PFJet30_v',
                                'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v', 
				]),
    prescales = cms.InputTag('patTrigger'),
    trigger = cms.InputTag("TriggerResults","","HLT"),
    objects = cms.InputTag('selectedPatTrigger'),
    ## CUSTOM CONFIGURATION
    onlyMc = cms.bool (False),  ## not completely supported yet

    #evt
    extendEvent = cms.untracked.bool(False),

    extendMet = cms.bool(True),
                      
    minJetPt  = cms.double (15.),
    minJetEta = cms.double (4.7),
    minJetN   = cms.int32  (0),
    minJetId  = cms.string ('loose'),
    matchJet  = cms.bool (True),
    matchJetDr = cms.double(0.3),

    ## PUPPI
    minPuppiJetPt  = cms.double (25.),
    minPuppiJetEta = cms.double (4.7),
    minPuppiJetN   = cms.int32  (0),
    minPuppiJetId  = cms.string ('loose'),
    
    ## CHS AK8
    minAK8CHSPt  = cms.double (100.),
    minAK8CHSEta = cms.double (4.7),
    minAK8CHSN   = cms.int32  (0),
    minAK8CHSId  = cms.string ('loose'),
    AK8CHSName   = cms.string ('AK8CHS'),

    ## Puppi AK8
    minAK8PuppiPt  = cms.double (100.),
    minAK8PuppiEta = cms.double (4.7),
    minAK8PuppiN   = cms.int32  (0),
    minAK8PuppiId  = cms.string ('loose'),
    AK8PuppiName   = cms.string ('AK8Puppi'),

    ## CHS CA15
    minCA15CHSPt  = cms.double (100.),
    minCA15CHSEta = cms.double (4.7),
    minCA15CHSN   = cms.int32  (0),
    minCA15CHSId  = cms.string ('loose'),
    CA15CHSName   = cms.string ('CA15CHS'),

    ## PUPPI CA15
    minCA15PuppiPt  = cms.double (100.),
    minCA15PuppiEta = cms.double (4.7),
    minCA15PuppiN   = cms.int32  (0),
    minCA15PuppiId  = cms.string ('loose'),
    CA15PuppiName   = cms.string ('CA15Puppi'),

    minElePt  = cms.double (10.),
    minEleEta = cms.double (2.5),
    maxEleIso = cms.double (-1.),

    minMuPt   = cms.double (10.),
    minMuEta  = cms.double (2.4),
    maxMuIso  = cms.double (-1),
   
    minLepN   = cms.int32 (0),
    matchLep  = cms.bool (True),
    matchLepDr = cms.double (0.1),

    minTauPt  = cms.double (18.),
    minTauEta = cms.double (2.3),
    minTauN   = cms.int32  (0),
    minTauId  = cms.string ('decayModeFindingNewDMs'),
    maxTauIso = cms.double (-1),
    extendTau = cms.bool(True),
    matchTau  = cms.bool (True),
    matchTauDr = cms.double (0.1),

    minGenParticlePt = cms.double(5.),
    minGenJetPt = cms.double(20.),
    particleGun = cms.untracked.bool(False),

    extendPhotons = cms.bool(True),                      
    minPhoPt  = cms.double (15.),
    minPhoEta = cms.double (2.5),
    minPhoN   = cms.int32  (0),
    maxPhoIso = cms.double (-1.),
    matchPho  = cms.bool (False),
    matchPhoDr = cms.double (0.3),
)
#------------------------------------------------------


