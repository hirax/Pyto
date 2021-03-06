"""
Classes from the 'MediaPlayer' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


_MPMiddlewareChainBuilderProxy = _Class("_MPMiddlewareChainBuilderProxy")
MPProtocolProxy = _Class("MPProtocolProxy")
_MPMusicPlayerMediaItemProxy = _Class("_MPMusicPlayerMediaItemProxy")
_MPStoreDownloadBlockObserver = _Class("_MPStoreDownloadBlockObserver")
MPStoreDownloadManager = _Class("MPStoreDownloadManager")
MPStoreDownload = _Class("MPStoreDownload")
MPStoreArtworkRequestToken = _Class("MPStoreArtworkRequestToken")
MPRestrictionsMonitor = _Class("MPRestrictionsMonitor")
MPArtworkConfiguration = _Class("MPArtworkConfiguration")
MPModelLibraryIncrementPlayCountChangeRequest = _Class(
    "MPModelLibraryIncrementPlayCountChangeRequest"
)
MPIdentifierSet = _Class("MPIdentifierSet")
MPMediaLibraryEntityTranslationContext = _Class(
    "MPMediaLibraryEntityTranslationContext"
)
MPMediaLibraryEntityTranslator = _Class("MPMediaLibraryEntityTranslator")
_MPMediaLibraryEntityRelationshipTranslator = _Class(
    "_MPMediaLibraryEntityRelationshipTranslator"
)
_MPMediaLibraryEntityPropertyTranslator = _Class(
    "_MPMediaLibraryEntityPropertyTranslator"
)
MPStoreSocialServiceTransientStatesSnapshot = _Class(
    "MPStoreSocialServiceTransientStatesSnapshot"
)
_MPStoreSocialTransientState = _Class("_MPStoreSocialTransientState")
MPStoreSocialServiceController = _Class("MPStoreSocialServiceController")
MPMusicPlayerControllerSystemCache = _Class("MPMusicPlayerControllerSystemCache")
MPExportableArtworkProperties = _Class("MPExportableArtworkProperties")
MPContentTastePendingUpdateRecord = _Class("MPContentTastePendingUpdateRecord")
MPPlaybackArchiveDisplayProperties = _Class("MPPlaybackArchiveDisplayProperties")
MPStoreOfferMediaItemArtworkDescriptor = _Class(
    "MPStoreOfferMediaItemArtworkDescriptor"
)
MPStoreContentReport = _Class("MPStoreContentReport")
MPStoreContentReporter = _Class("MPStoreContentReporter")
MPMediaEntityCache = _Class("MPMediaEntityCache")
MPUserNotification = _Class("MPUserNotification")
MPStoreLibraryPersonalizationContentDescriptor = _Class(
    "MPStoreLibraryPersonalizationContentDescriptor"
)
MPModelStorePlatformMetadataGenericObjectBuilder = _Class(
    "MPModelStorePlatformMetadataGenericObjectBuilder"
)
MPDetailScrubController = _Class("MPDetailScrubController")
MPMusicMediaPickerXPCInterfaces = _Class("MPMusicMediaPickerXPCInterfaces")
MPStoreSocialBlockOperationDataSource = _Class("MPStoreSocialBlockOperationDataSource")
_MPMediaLibraryArtworkVisualIdenticalityIdentifier = _Class(
    "_MPMediaLibraryArtworkVisualIdenticalityIdentifier"
)
_MPMediaLibraryArtworkDataSourceCacheKey = _Class(
    "_MPMediaLibraryArtworkDataSourceCacheKey"
)
MPMediaLibraryArtworkDataSource = _Class("MPMediaLibraryArtworkDataSource")
MPModelLibrarySearchEntityResultContainer = _Class(
    "MPModelLibrarySearchEntityResultContainer"
)
MPModelLibrarySearchSectionedCollectionDataSource = _Class(
    "MPModelLibrarySearchSectionedCollectionDataSource"
)
MPInlineVideoController = _Class("MPInlineVideoController")
MPStoreItemMetadataResponse = _Class("MPStoreItemMetadataResponse")
MPPropertySet = _Class("MPPropertySet")
MPMutablePropertySet = _Class("MPMutablePropertySet")
MPStoreItemMetadataCacheKey = _Class("MPStoreItemMetadataCacheKey")
MPStoreCompletionOfferResponse = _Class("MPStoreCompletionOfferResponse")
MPModelStoreBrowseResponseParser = _Class("MPModelStoreBrowseResponseParser")
MPRemoteCommand = _Class("MPRemoteCommand")
MPChangeQueueEndActionCommand = _Class("MPChangeQueueEndActionCommand")
MPSetPlaybackSessionCommand = _Class("MPSetPlaybackSessionCommand")
MPAdvanceRepeatModeCommand = _Class("MPAdvanceRepeatModeCommand")
MPAdvanceShuffleModeCommand = _Class("MPAdvanceShuffleModeCommand")
MPInsertIntoPlaybackQueueCommand = _Class("MPInsertIntoPlaybackQueueCommand")
MPReorderQueueCommand = _Class("MPReorderQueueCommand")
MPChangePlaybackPositionCommand = _Class("MPChangePlaybackPositionCommand")
MPSetPlaybackQueueCommand = _Class("MPSetPlaybackQueueCommand")
MPSkipTrackCommand = _Class("MPSkipTrackCommand")
MPChangeShuffleModeCommand = _Class("MPChangeShuffleModeCommand")
MPChangeRepeatModeCommand = _Class("MPChangeRepeatModeCommand")
MPChangePlaybackRateCommand = _Class("MPChangePlaybackRateCommand")
MPRatingCommand = _Class("MPRatingCommand")
MPFeedbackCommand = _Class("MPFeedbackCommand")
MPSkipIntervalCommand = _Class("MPSkipIntervalCommand")
_MPActiveUserChangeMonitor = _Class("_MPActiveUserChangeMonitor")
MPRadioStation = _Class("MPRadioStation")
MPNowPlayingInfoLanguageOptionGroup = _Class("MPNowPlayingInfoLanguageOptionGroup")
MPNowPlayingInfoLanguageOption = _Class("MPNowPlayingInfoLanguageOption")
_MPHomeSharingArtworkCacheKey = _Class("_MPHomeSharingArtworkCacheKey")
MPRadioLibrary = _Class("MPRadioLibrary")
MPLibraryAddStatusObserver = _Class("MPLibraryAddStatusObserver")
MPStorePlayWhileDownloadProperties = _Class("MPStorePlayWhileDownloadProperties")
MPStoreSocialUnfollowOperationDataSource = _Class(
    "MPStoreSocialUnfollowOperationDataSource"
)
MPStoreOfferContentRating = _Class("MPStoreOfferContentRating")
MPUbiquitousPlaybackPositionController = _Class(
    "MPUbiquitousPlaybackPositionController"
)
MPModelForYouRecommendationItemBuilder = _Class(
    "MPModelForYouRecommendationItemBuilder"
)
MPSSLookupResponseTransformContext = _Class("MPSSLookupResponseTransformContext")
MPStoreSocialRemoveFollowerOperationDataSource = _Class(
    "MPStoreSocialRemoveFollowerOperationDataSource"
)
MPNetworkObserver = _Class("MPNetworkObserver")
_MPModelLibraryDownloadQueueDataSource = _Class(
    "_MPModelLibraryDownloadQueueDataSource"
)
MPMediaControls = _Class("MPMediaControls")
MPStorePlatformEntityTranslatorContext = _Class(
    "MPStorePlatformEntityTranslatorContext"
)
MPModelLibraryPlaylistEditChangeRequest = _Class(
    "MPModelLibraryPlaylistEditChangeRequest"
)
MPStoreOffer = _Class("MPStoreOffer")
MPSectionedIdentifierListPosition = _Class("MPSectionedIdentifierListPosition")
_MPSectionedIdentifierListCloneIndexEntry = _Class(
    "_MPSectionedIdentifierListCloneIndexEntry"
)
_MPIdentifierListSectionProxy = _Class("_MPIdentifierListSectionProxy")
MPModelForYouRecommendationGroupBuilder = _Class(
    "MPModelForYouRecommendationGroupBuilder"
)
MPStoreItemMovieClipAsset = _Class("MPStoreItemMovieClipAsset")
MPMiddlewareChain = _Class("MPMiddlewareChain")
MPMiddlewareOperationMap = _Class("MPMiddlewareOperationMap")
MPStoreAssetInfoPlaybackCacheRequest = _Class("MPStoreAssetInfoPlaybackCacheRequest")
MPStoreAssetInfoPlaybackCache = _Class("MPStoreAssetInfoPlaybackCache")
MPArtworkColorAnalyzer = _Class("MPArtworkColorAnalyzer")
MPQueueFeederIdentifierRegistry = _Class("MPQueueFeederIdentifierRegistry")
MPTiledArtworkRepresentationToken = _Class("MPTiledArtworkRepresentationToken")
MPUbiquitousPlaybackPositionEntity = _Class("MPUbiquitousPlaybackPositionEntity")
MPModelLibraryIncrementSkipCountChangeRequest = _Class(
    "MPModelLibraryIncrementSkipCountChangeRequest"
)
MPStoreCompletionOfferingController = _Class("MPStoreCompletionOfferingController")
MPStoreCompletionOfferingLookupItem = _Class("MPStoreCompletionOfferingLookupItem")
MPModelForYouRecommendationMusicKitItemBuilder = _Class(
    "MPModelForYouRecommendationMusicKitItemBuilder"
)
MPStoreCollectionCompletionOffering = _Class("MPStoreCollectionCompletionOffering")
MPStoreCompletionOffering = _Class("MPStoreCompletionOffering")
MPRequestResponseController = _Class("MPRequestResponseController")
MPNetworkPlayabilityMonitor = _Class("MPNetworkPlayabilityMonitor")
MPGaplessInfo = _Class("MPGaplessInfo")
MPQueuePlayer = _Class("MPQueuePlayer")
MPModelLibraryImportChangeRequest = _Class("MPModelLibraryImportChangeRequest")
MPCloudController = _Class("MPCloudController")
MPCloudControllerItemIDList = _Class("MPCloudControllerItemIDList")
MPChangeDetails = _Class("MPChangeDetails")
MPStoreItemLibraryImport = _Class("MPStoreItemLibraryImport")
MPStoreItemLibraryImportElement = _Class("MPStoreItemLibraryImportElement")
MPStoreItemLibraryImportLookupElement = _Class("MPStoreItemLibraryImportLookupElement")
MPModelLibraryHasPurchasesRequest = _Class("MPModelLibraryHasPurchasesRequest")
MPStreamingDownloadSessionController = _Class("MPStreamingDownloadSessionController")
MPRemoteCommandCenter = _Class("MPRemoteCommandCenter")
_MPRemoteLaunchCommandCenter = _Class("_MPRemoteLaunchCommandCenter")
MPStoreRedownloadProductItemAsset = _Class("MPStoreRedownloadProductItemAsset")
MPModelForYouRecommendationMusicKitGroupBuilder = _Class(
    "MPModelForYouRecommendationMusicKitGroupBuilder"
)
MPPlayableContentManagerContext = _Class("MPPlayableContentManagerContext")
MPHomeSharingRentalTracker = _Class("MPHomeSharingRentalTracker")
MPStoreModelRequestConfiguration = _Class("MPStoreModelRequestConfiguration")
MPServerObjectDatabaseAsset = _Class("MPServerObjectDatabaseAsset")
_MPServerObjectDatabaseImporter = _Class("_MPServerObjectDatabaseImporter")
MPServerObjectDatabase = _Class("MPServerObjectDatabase")
MPModelPlaylistEntriesShareEligibilityRequest = _Class(
    "MPModelPlaylistEntriesShareEligibilityRequest"
)
MPMediaLibraryArtwork = _Class("MPMediaLibraryArtwork")
MPMediaLibraryArtworkRequest = _Class("MPMediaLibraryArtworkRequest")
MPMusicPlayerControllerApplicationQueueModifications = _Class(
    "MPMusicPlayerControllerApplicationQueueModifications"
)
MPMusicPlayerControllerNowPlaying = _Class("MPMusicPlayerControllerNowPlaying")
MPMusicPlayerControllerNowPlayingTimeSnapshot = _Class(
    "MPMusicPlayerControllerNowPlayingTimeSnapshot"
)
MPHSBrowserDelegate = _Class("MPHSBrowserDelegate")
MPSubscriptionStatusPlaybackInformation = _Class(
    "MPSubscriptionStatusPlaybackInformation"
)
MPNowPlayingInfoCenterArtworkContext = _Class("MPNowPlayingInfoCenterArtworkContext")
MPNowPlayingInfoTransportableSessionResponse = _Class(
    "MPNowPlayingInfoTransportableSessionResponse"
)
_MPNowPlayingInfoTransportableSessionRequest = _Class(
    "_MPNowPlayingInfoTransportableSessionRequest"
)
MPNowPlayingInfoCenter = _Class("MPNowPlayingInfoCenter")
_MPModelLibraryRegisteredTransientState = _Class(
    "_MPModelLibraryRegisteredTransientState"
)
MPModelLibraryTransientStateController = _Class(
    "MPModelLibraryTransientStateController"
)
_MPRTCReportingAVItemDeallocationHandler = _Class(
    "_MPRTCReportingAVItemDeallocationHandler"
)
MPRTCReportingController = _Class("MPRTCReportingController")
MPStoreSocialPendingFollowRequestOperationDataSource = _Class(
    "MPStoreSocialPendingFollowRequestOperationDataSource"
)
MPMediaQueryCriteria = _Class("MPMediaQueryCriteria")
MPModelVerifyLocalFileAssetIntegrityRequest = _Class(
    "MPModelVerifyLocalFileAssetIntegrityRequest"
)
MPPThreadKeyExclusiveAccessToken = _Class("MPPThreadKeyExclusiveAccessToken")
MPDispatchQueueExclusiveAccessToken = _Class("MPDispatchQueueExclusiveAccessToken")
MPModelStoreBrowseRoomMusicKitResponseParser = _Class(
    "MPModelStoreBrowseRoomMusicKitResponseParser"
)
MPCloudServiceStatusController = _Class("MPCloudServiceStatusController")
MPStoreAssetPlaybackResponse = _Class("MPStoreAssetPlaybackResponse")
MPMutableStoreAssetPlaybackResponse = _Class("MPMutableStoreAssetPlaybackResponse")
MPNowPlayingInfoQueueCoordinator = _Class("MPNowPlayingInfoQueueCoordinator")
MPVolumeHUDController = _Class("MPVolumeHUDController")
MPPlaybackUserDefaults = _Class("MPPlaybackUserDefaults")
MPAVBatteryLevel = _Class("MPAVBatteryLevel")
MPStoreRadioStreamAssetInfo = _Class("MPStoreRadioStreamAssetInfo")
MPMediaLibrarySystemFilters = _Class("MPMediaLibrarySystemFilters")
MPVolumeGroupSliderCoordinator = _Class("MPVolumeGroupSliderCoordinator")
MPArtworkColorAnalysis = _Class("MPArtworkColorAnalysis")
MPMutableArtworkColorAnalysis = _Class("MPMutableArtworkColorAnalysis")
MPContentItem = _Class("MPContentItem")
MPNowPlayingContentItem = _Class("MPNowPlayingContentItem")
MPBrowsableContentItem = _Class("MPBrowsableContentItem")
MPRandomDistribution = _Class("MPRandomDistribution")
MPARC4RandomSource = _Class("MPARC4RandomSource")
MPMediaQuerySection = _Class("MPMediaQuerySection")
MPModelLibraryHasBeenPlayedChangeRequest = _Class(
    "MPModelLibraryHasBeenPlayedChangeRequest"
)
MPVolumeHardwareButtonController = _Class("MPVolumeHardwareButtonController")
MPPlaceholderArtwork = _Class("MPPlaceholderArtwork")
_MPKeyPathEntityRelationshipTranslator = _Class(
    "_MPKeyPathEntityRelationshipTranslator"
)
_MPStorePlatformEntityRelationshipTranslator = _Class(
    "_MPStorePlatformEntityRelationshipTranslator"
)
_MPMediaKitEntityRelationshipTranslator = _Class(
    "_MPMediaKitEntityRelationshipTranslator"
)
_MPKeyPathEntityPropertyTranslator = _Class("_MPKeyPathEntityPropertyTranslator")
_MPStorePlatformEntityPropertyTranslator = _Class(
    "_MPStorePlatformEntityPropertyTranslator"
)
_MPMediaKitEntityPropertyTranslator = _Class("_MPMediaKitEntityPropertyTranslator")
MPMediaKitEntityTranslatorContext = _Class("MPMediaKitEntityTranslatorContext")
MPMediaKitEntityPayloadTransformer = _Class("MPMediaKitEntityPayloadTransformer")
MPStoreLibraryMappingResponse = _Class("MPStoreLibraryMappingResponse")
MPStoreDownloadExpectationController = _Class("MPStoreDownloadExpectationController")
MPAVRoute = _Class("MPAVRoute")
MPAVEndpointRoute = _Class("MPAVEndpointRoute")
MPAVOutputDeviceRoute = _Class("MPAVOutputDeviceRoute")
MPAVTelevisionRoute = _Class("MPAVTelevisionRoute")
MPAVOutputDeviceDescription = _Class("MPAVOutputDeviceDescription")
_MPBaseEntityRelationshipTranslator = _Class("_MPBaseEntityRelationshipTranslator")
MPKeyValueObserver = _Class("MPKeyValueObserver")
MPStoreLibraryPersonalizationCollectionDataSource = _Class(
    "MPStoreLibraryPersonalizationCollectionDataSource"
)
MPMediaChapter = _Class("MPMediaChapter")
MPVolumeControllerRouteDataSource = _Class("MPVolumeControllerRouteDataSource")
MPVolumeControllerSystemDataSource = _Class("MPVolumeControllerSystemDataSource")
MPVolumeController = _Class("MPVolumeController")
MPStorePlayWhileDownloadController = _Class("MPStorePlayWhileDownloadController")
MPMediaQuerySectionInfo = _Class("MPMediaQuerySectionInfo")
MPMediaQueryMutableSectionInfo = _Class("MPMediaQueryMutableSectionInfo")
MPStreamingDownloadSessionRequest = _Class("MPStreamingDownloadSessionRequest")
MPStoreFileAssetFairPlayInfo = _Class("MPStoreFileAssetFairPlayInfo")
MPModelLibraryAlbumAppDataChangeRequest = _Class(
    "MPModelLibraryAlbumAppDataChangeRequest"
)
MPAVRouteConnection = _Class("MPAVRouteConnection")
MPMediaLibraryDataProviderML3 = _Class("MPMediaLibraryDataProviderML3")
MPHomeSharingML3DataProvider = _Class("MPHomeSharingML3DataProvider")
MPMediaLibraryDataProviderSystemML3 = _Class("MPMediaLibraryDataProviderSystemML3")
MPConcreteMediaEntityPropertiesCache = _Class("MPConcreteMediaEntityPropertiesCache")
MPCFWrapper = _Class("MPCFWrapper")
MPMRAVEndpointObserverWrapper = _Class("MPMRAVEndpointObserverWrapper")
MPMRAVOutputContextWrapper = _Class("MPMRAVOutputContextWrapper")
MPMRAVEndpointWrapper = _Class("MPMRAVEndpointWrapper")
MPAVRoutingViewItem = _Class("MPAVRoutingViewItem")
MPAVErrorResolver = _Class("MPAVErrorResolver")
MPStorePurchaseErrorResolver = _Class("MPStorePurchaseErrorResolver")
MPHomeSharingRentalErrorResolver = _Class("MPHomeSharingRentalErrorResolver")
MPHomeSharingErrorResolver = _Class("MPHomeSharingErrorResolver")
MPModelLibraryModelSectionedCollectionDataSource = _Class(
    "MPModelLibraryModelSectionedCollectionDataSource"
)
MPMusicPlayerPlayParameters = _Class("MPMusicPlayerPlayParameters")
MPMusicPlayerQueueDescriptor = _Class("MPMusicPlayerQueueDescriptor")
MPMusicPlayerPlaybackArchiveQueueDescriptor = _Class(
    "MPMusicPlayerPlaybackArchiveQueueDescriptor"
)
MPMusicPlayerRadioStationQueueDescriptor = _Class(
    "MPMusicPlayerRadioStationQueueDescriptor"
)
MPMusicPlayerPlayParametersQueueDescriptor = _Class(
    "MPMusicPlayerPlayParametersQueueDescriptor"
)
MPMusicPlayerStoreQueueDescriptor = _Class("MPMusicPlayerStoreQueueDescriptor")
MPMusicPlayerMediaItemQueueDescriptor = _Class("MPMusicPlayerMediaItemQueueDescriptor")
_MPAbstractNetworkArtworkDataSourceVisualIdenticalityIdentifier = _Class(
    "_MPAbstractNetworkArtworkDataSourceVisualIdenticalityIdentifier"
)
MPAVAuxiliaryDevice = _Class("MPAVAuxiliaryDevice")
MPStoreSocialFollowOperationDataSource = _Class(
    "MPStoreSocialFollowOperationDataSource"
)
MPNowPlayingInfoLyricsEvent = _Class("MPNowPlayingInfoLyricsEvent")
MPNowPlayingInfoLyricsItem = _Class("MPNowPlayingInfoLyricsItem")
MPNowPlayingInfoLyricsItemToken = _Class("MPNowPlayingInfoLyricsItemToken")
MPStoreItemMetadataCache = _Class("MPStoreItemMetadataCache")
MPStoreItemOfferAsset = _Class("MPStoreItemOfferAsset")
MPRemoteRadioController = _Class("MPRemoteRadioController")
MPAVRoutingViewControllerUpdate = _Class("MPAVRoutingViewControllerUpdate")
MPAVRoutingViewControllerItems = _Class("MPAVRoutingViewControllerItems")
MPAVRoutingViewControllerUpdateDisplayedRoutesState = _Class(
    "MPAVRoutingViewControllerUpdateDisplayedRoutesState"
)
_MPLazySectionedCollectionStorage = _Class("_MPLazySectionedCollectionStorage")
MPAudioDeviceController = _Class("MPAudioDeviceController")
MPMediaAPIParserLayer = _Class("MPMediaAPIParserLayer")
MPPlayableContentCallbackContext = _Class("MPPlayableContentCallbackContext")
MPPlayableContentManager = _Class("MPPlayableContentManager")
MPMusicPlayerControllerQueue = _Class("MPMusicPlayerControllerQueue")
MPMusicPlayerControllerMutableQueue = _Class("MPMusicPlayerControllerMutableQueue")
MPAVErrorResolverBlockHandler = _Class("MPAVErrorResolverBlockHandler")
MPMediaDownload = _Class("MPMediaDownload")
MPNotificationObserver = _Class("MPNotificationObserver")
MPLibraryKeepLocalStatusObserverConfiguration = _Class(
    "MPLibraryKeepLocalStatusObserverConfiguration"
)
MPLibraryKeepLocalStatusObserverIndividualEntityConfiguration = _Class(
    "MPLibraryKeepLocalStatusObserverIndividualEntityConfiguration"
)
MPLibraryKeepLocalStatusObserverDetailedContainerConfiguration = _Class(
    "MPLibraryKeepLocalStatusObserverDetailedContainerConfiguration"
)
MPLibraryKeepLocalStatusObserver = _Class("MPLibraryKeepLocalStatusObserver")
MPAVQueueCoordinator = _Class("MPAVQueueCoordinator")
MPMediaPickerConfiguration = _Class("MPMediaPickerConfiguration")
MPMediaPickerController_Appex = _Class("MPMediaPickerController_Appex")
_MPMediaLibraryEntityChange = _Class("_MPMediaLibraryEntityChange")
MPMediaLibraryConnectionAssertion = _Class("MPMediaLibraryConnectionAssertion")
MPMediaLibrary = _Class("MPMediaLibrary")
MPMediaItemArtwork = _Class("MPMediaItemArtwork")
MPConcreteMediaItemArtwork = _Class("MPConcreteMediaItemArtwork")
MPStoreOfferMediaItemArtwork = _Class("MPStoreOfferMediaItemArtwork")
_MPArtworkCatalogStaticDataSource = _Class("_MPArtworkCatalogStaticDataSource")
_MPStaticArtworkVisualIdenticalityIdentifier = _Class(
    "_MPStaticArtworkVisualIdenticalityIdentifier"
)
MPArtworkRepresentationCollection = _Class("MPArtworkRepresentationCollection")
MPArtworkRepresentation = _Class("MPArtworkRepresentation")
MPArtworkCatalog = _Class("MPArtworkCatalog")
MPMusicPlayerController = _Class("MPMusicPlayerController")
MPMusicPlayerSystemController = _Class("MPMusicPlayerSystemController")
MPMusicPlayerApplicationController = _Class("MPMusicPlayerApplicationController")
MPMediaPredicate = _Class("MPMediaPredicate")
_MPMediaSearchStringPredicate = _Class("_MPMediaSearchStringPredicate")
MPMediaPersistentIDsPredicate = _Class("MPMediaPersistentIDsPredicate")
MPMediaContainmentPredicate = _Class("MPMediaContainmentPredicate")
MPMediaCompoundPredicate = _Class("MPMediaCompoundPredicate")
MPMediaCompoundAnyPredicate = _Class("MPMediaCompoundAnyPredicate")
MPMediaCompoundAllPredicate = _Class("MPMediaCompoundAllPredicate")
MPMediaConditionalPredicate = _Class("MPMediaConditionalPredicate")
MPMediaPropertyPredicate = _Class("MPMediaPropertyPredicate")
MPMediaQuery = _Class("MPMediaQuery")
MPPlaybackArchive = _Class("MPPlaybackArchive")
MPPlaybackArchiveConfiguration = _Class("MPPlaybackArchiveConfiguration")
MPMediaPlaylistCreationMetadata = _Class("MPMediaPlaylistCreationMetadata")
MPMediaEntity = _Class("MPMediaEntity")
MPMediaItem = _Class("MPMediaItem")
MPConcreteMediaItem = _Class("MPConcreteMediaItem")
MPNondurableMediaItem = _Class("MPNondurableMediaItem")
MPStorePlatformMediaItem = _Class("MPStorePlatformMediaItem")
MPStoreOfferMediaItem = _Class("MPStoreOfferMediaItem")
MPModelObjectMediaItem = _Class("MPModelObjectMediaItem")
MPMediaItemCollection = _Class("MPMediaItemCollection")
MPStoreOfferMediaItemCollection = _Class("MPStoreOfferMediaItemCollection")
MPConcreteMediaItemCollection = _Class("MPConcreteMediaItemCollection")
MPMediaPlaylist = _Class("MPMediaPlaylist")
MPConcreteMediaPlaylist = _Class("MPConcreteMediaPlaylist")
MPStoreItemMetadataRequestController = _Class("MPStoreItemMetadataRequestController")
MPContentTasteController = _Class("MPContentTasteController")
MPPlaybackContext = _Class("MPPlaybackContext")
MPModelStoreBrowseSectionUniformContentItemTypeResolver = _Class(
    "MPModelStoreBrowseSectionUniformContentItemTypeResolver"
)
_MPMediaLibraryMLCoreStorage = _Class("_MPMediaLibraryMLCoreStorage")
_MPModelShimRequestMiddleware = _Class("_MPModelShimRequestMiddleware")
MPServerObjectDatabaseImportResult = _Class("MPServerObjectDatabaseImportResult")
MPServerObjectDatabaseImportRequest = _Class("MPServerObjectDatabaseImportRequest")
MPServerObjectDatabaseAssetImportRequest = _Class(
    "MPServerObjectDatabaseAssetImportRequest"
)
MPServerObjectDatabaseSINFImportRequest = _Class(
    "MPServerObjectDatabaseSINFImportRequest"
)
MPServerObjectDatabaseSubPlaybackDispatchImportRequest = _Class(
    "MPServerObjectDatabaseSubPlaybackDispatchImportRequest"
)
MPServerObjectDatabaseMetadataImportRequest = _Class(
    "MPServerObjectDatabaseMetadataImportRequest"
)
MPServerObjectDatabaseStorePlatformImportRequest = _Class(
    "MPServerObjectDatabaseStorePlatformImportRequest"
)
MPServerObjectDatabaseMediaKitImportRequest = _Class(
    "MPServerObjectDatabaseMediaKitImportRequest"
)
MPAbstractNetworkArtworkDataSource = _Class("MPAbstractNetworkArtworkDataSource")
MPHomeSharingArtworkDataSource = _Class("MPHomeSharingArtworkDataSource")
MPStoreArtworkDataSource = _Class("MPStoreArtworkDataSource")
MPCompleteMyCollectionArtworkDataSource = _Class(
    "MPCompleteMyCollectionArtworkDataSource"
)
MPAVRoutingControllerSelectionQueue = _Class("MPAVRoutingControllerSelectionQueue")
MPAVRoutingControllerSelection = _Class("MPAVRoutingControllerSelection")
MPAVRoutingController = _Class("MPAVRoutingController")
MPMediaControlsLanguageOptions = _Class("MPMediaControlsLanguageOptions")
MPModelLibraryDefaultSectionedCollectionDataSource = _Class(
    "MPModelLibraryDefaultSectionedCollectionDataSource"
)
MPRemoteCommandEvent = _Class("MPRemoteCommandEvent")
MPChangeQueueEndActionCommandEvent = _Class("MPChangeQueueEndActionCommandEvent")
MPSetPlaybackSessionCommandEvent = _Class("MPSetPlaybackSessionCommandEvent")
MPAdvanceRepeatModeCommandEvent = _Class("MPAdvanceRepeatModeCommandEvent")
MPAdvanceShuffleModeCommandEvent = _Class("MPAdvanceShuffleModeCommandEvent")
MPChangeLanguageOptionCommandEvent = _Class("MPChangeLanguageOptionCommandEvent")
MPInsertIntoPlaybackQueueCommandEvent = _Class("MPInsertIntoPlaybackQueueCommandEvent")
MPReorderQueueCommandEvent = _Class("MPReorderQueueCommandEvent")
MPSetPlaybackQueueCommandEvent = _Class("MPSetPlaybackQueueCommandEvent")
MPCreateRadioStationCommandEvent = _Class("MPCreateRadioStationCommandEvent")
MPChangeShuffleModeCommandEvent = _Class("MPChangeShuffleModeCommandEvent")
MPChangeRepeatModeCommandEvent = _Class("MPChangeRepeatModeCommandEvent")
MPChangePlaybackPositionCommandEvent = _Class("MPChangePlaybackPositionCommandEvent")
MPSpecialSeekCommandEvent = _Class("MPSpecialSeekCommandEvent")
MPSkipTrackCommandEvent = _Class("MPSkipTrackCommandEvent")
MPFeedbackCommandEvent = _Class("MPFeedbackCommandEvent")
MPChangePlaybackRateCommandEvent = _Class("MPChangePlaybackRateCommandEvent")
MPRatingCommandEvent = _Class("MPRatingCommandEvent")
MPSeekCommandEvent = _Class("MPSeekCommandEvent")
MPSkipIntervalCommandEvent = _Class("MPSkipIntervalCommandEvent")
MPSectionedIdentifierListEntry = _Class("MPSectionedIdentifierListEntry")
MPSectionedIdentifierListItemEntry = _Class("MPSectionedIdentifierListItemEntry")
MPSectionedIdentifierListHeadEntry = _Class("MPSectionedIdentifierListHeadEntry")
MPSectionedIdentifierListTailEntry = _Class("MPSectionedIdentifierListTailEntry")
MPSectionedIdentifierListEntryPositionKey = _Class(
    "MPSectionedIdentifierListEntryPositionKey"
)
MPStorePlayWhileDownloadSession = _Class("MPStorePlayWhileDownloadSession")
MPStreamingDownloadSession = _Class("MPStreamingDownloadSession")
MPModelLibraryResponseKeepLocalStatusConfiguration = _Class(
    "MPModelLibraryResponseKeepLocalStatusConfiguration"
)
MPStoreHLSAssetInfo = _Class("MPStoreHLSAssetInfo")
_MPSectionedIdentifierListProxyEntry = _Class("_MPSectionedIdentifierListProxyEntry")
MPStoreRedownloadProductItem = _Class("MPStoreRedownloadProductItem")
MPMediaControlsStatusBarStyleOverridesCoordinator = _Class(
    "MPMediaControlsStatusBarStyleOverridesCoordinator"
)
MPSectionedCollection = _Class("MPSectionedCollection")
MPLazySectionedCollection = _Class("MPLazySectionedCollection")
MPMutableSectionedCollection = _Class("MPMutableSectionedCollection")
MPAVLightweightRoutingController = _Class("MPAVLightweightRoutingController")
MPArtworkResizeUtility = _Class("MPArtworkResizeUtility")
MPModelLibraryAddToPlaylistChangeRequest = _Class(
    "MPModelLibraryAddToPlaylistChangeRequest"
)
MPModelRequest = _Class("MPModelRequest")
MPModelLibraryDownloadQueueRequest = _Class("MPModelLibraryDownloadQueueRequest")
MPStoreLibraryPersonalizationRequest = _Class("MPStoreLibraryPersonalizationRequest")
MPModelStaticRequest = _Class("MPModelStaticRequest")
MPModelLibraryRequest = _Class("MPModelLibraryRequest")
MPModelLibrarySearchRequest = _Class("MPModelLibrarySearchRequest")
MPStoreModelRequest = _Class("MPStoreModelRequest")
MPModelStoreBrowseRoomRequest = _Class("MPModelStoreBrowseRoomRequest")
MPModelStoreBrowseRequest = _Class("MPModelStoreBrowseRequest")
MPModelForYouRecommendationsRequest = _Class("MPModelForYouRecommendationsRequest")
MPModelRecentlyPlayedRequest = _Class("MPModelRecentlyPlayedRequest")
MPModelLibrarySearchScope = _Class("MPModelLibrarySearchScope")
_MPSSILImplementationInitToken = _Class("_MPSSILImplementationInitToken")
MPSectionedIdentifierList = _Class("MPSectionedIdentifierList")
_MPSSILImplementation = _Class("_MPSSILImplementation")
MPShuffleableSectionedIdentifierList = _Class("MPShuffleableSectionedIdentifierList")
MPModelStoreGroupingsMusicKitResponseParser = _Class(
    "MPModelStoreGroupingsMusicKitResponseParser"
)
MPModelStoreBrowseSectionBuilder = _Class("MPModelStoreBrowseSectionBuilder")
MPRadioRecentStationsGroup = _Class("MPRadioRecentStationsGroup")
MPStoreLyricsRequest = _Class("MPStoreLyricsRequest")
MPRemotePlaybackQueue = _Class("MPRemotePlaybackQueue")
MPPlaybackContextRemotePlaybackQueue = _Class("MPPlaybackContextRemotePlaybackQueue")
MPEmptyPlaybackQueue = _Class("MPEmptyPlaybackQueue")
MPCustomDataPlaybackQueue = _Class("MPCustomDataPlaybackQueue")
MPGeniusPlaybackQueue = _Class("MPGeniusPlaybackQueue")
MPGenericTracklistPlaybackQueue = _Class("MPGenericTracklistPlaybackQueue")
MPRadioStationRemotePlaybackQueue = _Class("MPRadioStationRemotePlaybackQueue")
MPLocalMediaQueryRemotePlaybackQueue = _Class("MPLocalMediaQueryRemotePlaybackQueue")
MPAVRoutingTableViewCellSubtitleTextState = _Class(
    "MPAVRoutingTableViewCellSubtitleTextState"
)
MPTiledArtworkRepresentationCacheKey = _Class("MPTiledArtworkRepresentationCacheKey")
MPAVPolicyEnforcer = _Class("MPAVPolicyEnforcer")
MPModelLibraryKeepLocalChangeRequest = _Class("MPModelLibraryKeepLocalChangeRequest")
MPWeakTimer = _Class("MPWeakTimer")
MPBaseEntityTranslator = _Class("MPBaseEntityTranslator")
MPStorePlatformEntityTranslator = _Class("MPStorePlatformEntityTranslator")
MPMediaKitEntityTranslator = _Class("MPMediaKitEntityTranslator")
MPMediaRemoteEntityTranslator = _Class("MPMediaRemoteEntityTranslator")
_MPMediaRemoteEntityPropertyTranslator = _Class(
    "_MPMediaRemoteEntityPropertyTranslator"
)
MPMediaRemoteEntityTranslatorContext = _Class("MPMediaRemoteEntityTranslatorContext")
MPStoreFileAssetInfo = _Class("MPStoreFileAssetInfo")
MPMediaLibraryAlbumAppData = _Class("MPMediaLibraryAlbumAppData")
MPAssistantMusicLogEvent = _Class("MPAssistantMusicLogEvent")
MPAssistantMusicAssetLoadLogEvent = _Class("MPAssistantMusicAssetLoadLogEvent")
MPAssistantMusicSummaryLogEvent = _Class("MPAssistantMusicSummaryLogEvent")
MPAVRoutingDataSource = _Class("MPAVRoutingDataSource")
MPAVOutputDeviceRoutingDataSource = _Class("MPAVOutputDeviceRoutingDataSource")
MPAVEndpointRoutingDataSource = _Class("MPAVEndpointRoutingDataSource")
MPAVTelevisionRoutingDataSource = _Class("MPAVTelevisionRoutingDataSource")
MPRadioController = _Class("MPRadioController")
MPRadioStationEvent = _Class("MPRadioStationEvent")
MPStoreRedownloadProductResponse = _Class("MPStoreRedownloadProductResponse")
MPStoreItemMovieClip = _Class("MPStoreItemMovieClip")
MPStoreItemOffer = _Class("MPStoreItemOffer")
MPAVController = _Class("MPAVController")
MPMediaPlaybackItemMetadata = _Class("MPMediaPlaybackItemMetadata")
MPMediaLibraryPlaybackItemMetadata = _Class("MPMediaLibraryPlaybackItemMetadata")
MPModelObjectPlaybackItemMetadata = _Class("MPModelObjectPlaybackItemMetadata")
MPModelSongPlaybackItemMetadata = _Class("MPModelSongPlaybackItemMetadata")
MPModelPlaylistEntrySongPlaybackItemMetadata = _Class(
    "MPModelPlaylistEntrySongPlaybackItemMetadata"
)
MPModelMoviePlaybackItemMetadata = _Class("MPModelMoviePlaybackItemMetadata")
MPModelPlaylistEntryMoviePlaybackItemMetadata = _Class(
    "MPModelPlaylistEntryMoviePlaybackItemMetadata"
)
MPModelTVEpisodePlaybackItemMetadata = _Class("MPModelTVEpisodePlaybackItemMetadata")
MPModelPlaylistEntryTVEpisodePlaybackItemMetadata = _Class(
    "MPModelPlaylistEntryTVEpisodePlaybackItemMetadata"
)
MPTiledArtworkDataSource = _Class("MPTiledArtworkDataSource")
MPTimeMarker = _Class("MPTimeMarker")
MPMediaChapterTimeMarker = _Class("MPMediaChapterTimeMarker")
MPStoreItemMetadata = _Class("MPStoreItemMetadata")
MPModelLibraryDeleteEntityChangeRequest = _Class(
    "MPModelLibraryDeleteEntityChangeRequest"
)
MPQueueFeeder = _Class("MPQueueFeeder")
MPStoreItemMetadataRequest = _Class("MPStoreItemMetadataRequest")
MPAVItem = _Class("MPAVItem")
MPPlaceholderAVItem = _Class("MPPlaceholderAVItem")
MPRTCReportingEvent = _Class("MPRTCReportingEvent")
MPRTCReportingNetworkInterfaceChangeEvent = _Class(
    "MPRTCReportingNetworkInterfaceChangeEvent"
)
MPRTCReportingAssetLoadEvent = _Class("MPRTCReportingAssetLoadEvent")
MPRTCReportingSecureKeyLoadEvent = _Class("MPRTCReportingSecureKeyLoadEvent")
MPRTCReportingSessionSummaryEvent = _Class("MPRTCReportingSessionSummaryEvent")
MPTiledArtworkRequest = _Class("MPTiledArtworkRequest")
MPAlternateTracks = _Class("MPAlternateTracks")
MPRTCReportingSession = _Class("MPRTCReportingSession")
MPAlternateTrack = _Class("MPAlternateTrack")
MPAlternateTextTrack = _Class("MPAlternateTextTrack")
MPAssistantAnalyticsReportingController = _Class(
    "MPAssistantAnalyticsReportingController"
)
MPMovieErrorLogEvent = _Class("MPMovieErrorLogEvent")
MPMovieAccessLogEvent = _Class("MPMovieAccessLogEvent")
MPMovieErrorLog = _Class("MPMovieErrorLog")
MPMovieAccessLog = _Class("MPMovieAccessLog")
MPTimedMetadata = _Class("MPTimedMetadata")
MPMoviePlayerController = _Class("MPMoviePlayerController")
MPModelObject = _Class("MPModelObject")
MPModelAlbum = _Class("MPModelAlbum")
MPModelPodcastEpisode = _Class("MPModelPodcastEpisode")
MPModelTVShow = _Class("MPModelTVShow")
MPModelStoreAsset = _Class("MPModelStoreAsset")
MPModelFileAsset = _Class("MPModelFileAsset")
MPModelTVSeason = _Class("MPModelTVSeason")
MPModelStoreBrowseSection = _Class("MPModelStoreBrowseSection")
MPModelPlaylistEntry = _Class("MPModelPlaylistEntry")
MPModelForYouRecommendationGroup = _Class("MPModelForYouRecommendationGroup")
MPModelPlaybackPosition = _Class("MPModelPlaybackPosition")
MPModelGenre = _Class("MPModelGenre")
MPModelPlaylist = _Class("MPModelPlaylist")
MPModelGenericObject = _Class("MPModelGenericObject")
MPModelHomeSharingAsset = _Class("MPModelHomeSharingAsset")
MPModelForYouRecommendationItem = _Class("MPModelForYouRecommendationItem")
MPModelStoreBrowseContentItem = _Class("MPModelStoreBrowseContentItem")
MPModelPodcast = _Class("MPModelPodcast")
MPModelRadioStation = _Class("MPModelRadioStation")
MPModelMovie = _Class("MPModelMovie")
MPModelMediaClip = _Class("MPModelMediaClip")
MPModelStaticAsset = _Class("MPModelStaticAsset")
MPModelTVEpisode = _Class("MPModelTVEpisode")
MPModelPlayEvent = _Class("MPModelPlayEvent")
MPModelPerson = _Class("MPModelPerson")
MPModelSocialPerson = _Class("MPModelSocialPerson")
MPModelCurator = _Class("MPModelCurator")
MPModelTVShowCreator = _Class("MPModelTVShowCreator")
MPModelComposer = _Class("MPModelComposer")
MPModelArtist = _Class("MPModelArtist")
_MPModelLibraryItemArtist = _Class("_MPModelLibraryItemArtist")
_MPModelMediaRemoteItemArtist = _Class("_MPModelMediaRemoteItemArtist")
MPModelPodcastAuthor = _Class("MPModelPodcastAuthor")
_MPModelLibraryPodcastEpisodeAuthor = _Class("_MPModelLibraryPodcastEpisodeAuthor")
_MPModelMediaRemotePodcastEpisodeAuthor = _Class(
    "_MPModelMediaRemotePodcastEpisodeAuthor"
)
MPModelSong = _Class("MPModelSong")
MPModelLyrics = _Class("MPModelLyrics")
MPModelKind = _Class("MPModelKind")
MPModelAlbumKind = _Class("MPModelAlbumKind")
MPModelPodcastEpisodeKind = _Class("MPModelPodcastEpisodeKind")
MPModelSocialPersonKind = _Class("MPModelSocialPersonKind")
MPModelTVShowKind = _Class("MPModelTVShowKind")
MPModelFileAssetKind = _Class("MPModelFileAssetKind")
MPModelTVSeasonKind = _Class("MPModelTVSeasonKind")
MPModelPlaylistEntryKind = _Class("MPModelPlaylistEntryKind")
MPModelForYouRecommendationGroupKind = _Class("MPModelForYouRecommendationGroupKind")
MPModelGenreKind = _Class("MPModelGenreKind")
MPModelPlaylistKind = _Class("MPModelPlaylistKind")
MPModelCuratorActualKind = _Class("MPModelCuratorActualKind")
MPModelGenericObjectKind = _Class("MPModelGenericObjectKind")
MPModelPodcastKind = _Class("MPModelPodcastKind")
MPModelRadioStationKind = _Class("MPModelRadioStationKind")
MPModelMovieKind = _Class("MPModelMovieKind")
MPModelMediaClipKind = _Class("MPModelMediaClipKind")
MPModelStaticAssetKind = _Class("MPModelStaticAssetKind")
MPModelTVEpisodeKind = _Class("MPModelTVEpisodeKind")
MPModelComposerKind = _Class("MPModelComposerKind")
MPModelArtistKind = _Class("MPModelArtistKind")
MPModelSongKind = _Class("MPModelSongKind")
MPModelLyricsKind = _Class("MPModelLyricsKind")
MPModelResponse = _Class("MPModelResponse")
MPModelLibraryDownloadQueueResponse = _Class("MPModelLibraryDownloadQueueResponse")
MPStoreLibraryPersonalizationResponse = _Class("MPStoreLibraryPersonalizationResponse")
MPModelStaticResponse = _Class("MPModelStaticResponse")
MPModelRecentlyPlayedResponse = _Class("MPModelRecentlyPlayedResponse")
MPModelLibraryResponse = _Class("MPModelLibraryResponse")
MPModelLibrarySearchResponse = _Class("MPModelLibrarySearchResponse")
MPModelForYouRecommendationsResponse = _Class("MPModelForYouRecommendationsResponse")
MPModelStoreBrowseResponse = _Class("MPModelStoreBrowseResponse")
MPResponse = _Class("MPResponse")
MPModelShimResponse = _Class("MPModelShimResponse")
MPRequest = _Class("MPRequest")
MPModelShimRequest = _Class("MPModelShimRequest")
MPMediaLibraryView = _Class("MPMediaLibraryView")
MPStoreSocialUnblockOperationDataSource = _Class(
    "MPStoreSocialUnblockOperationDataSource"
)
MPMediaControlsConfiguration = _Class("MPMediaControlsConfiguration")
MPMediaDownloadManager = _Class("MPMediaDownloadManager")
MPStoreModelObjectBuilder = _Class("MPStoreModelObjectBuilder")
MPStoreModelSocialPersonBuilder = _Class("MPStoreModelSocialPersonBuilder")
MPStoreModelMovieBuilder = _Class("MPStoreModelMovieBuilder")
MPStoreModelTVShowCreatorBuilder = _Class("MPStoreModelTVShowCreatorBuilder")
MPStoreModelTVSeasonBuilder = _Class("MPStoreModelTVSeasonBuilder")
MPStoreModelCuratorBuilder = _Class("MPStoreModelCuratorBuilder")
MPStoreModelStoreAssetBuilder = _Class("MPStoreModelStoreAssetBuilder")
MPStoreModelGenericObjectBuilder = _Class("MPStoreModelGenericObjectBuilder")
MPStoreModelTVEpisodeBuilder = _Class("MPStoreModelTVEpisodeBuilder")
MPStoreModelPlaybackPositionBuilder = _Class("MPStoreModelPlaybackPositionBuilder")
MPStoreModelSongBuilder = _Class("MPStoreModelSongBuilder")
MPStoreModelArtistBuilder = _Class("MPStoreModelArtistBuilder")
MPStoreModelMovieMediaClipBuilder = _Class("MPStoreModelMovieMediaClipBuilder")
MPStoreModelPlaylistBuilder = _Class("MPStoreModelPlaylistBuilder")
MPStoreModelTVShowBuilder = _Class("MPStoreModelTVShowBuilder")
MPStoreModelAlbumBuilder = _Class("MPStoreModelAlbumBuilder")
MPStoreModelRadioStationBuilder = _Class("MPStoreModelRadioStationBuilder")
MPModelStoreBrowseContentItemBuilder = _Class("MPModelStoreBrowseContentItemBuilder")
MPStoreItemImportTrackData = _Class("MPStoreItemImportTrackData")
MPAudioVideoRoutingPopoverController = _Class("MPAudioVideoRoutingPopoverController")
MPPMediaPredicate = _Class("MPPMediaPredicate")
MPPMediaPredicateValue = _Class("MPPMediaPredicateValue")
MPPPersistentIDsPredicate = _Class("MPPPersistentIDsPredicate")
MPPPropertyPredicate = _Class("MPPPropertyPredicate")
MPPMediaQuery = _Class("MPPMediaQuery")
MPPSearchStringPredicate = _Class("MPPSearchStringPredicate")
MPPConditionalPredicate = _Class("MPPConditionalPredicate")
MPPCompoundPredicate = _Class("MPPCompoundPredicate")
MPCubicSpringTimingParameters = _Class("MPCubicSpringTimingParameters")
MPCubicSpringAnimator = _Class("MPCubicSpringAnimator")
_MPArtworkDataSourceURLCache = _Class("_MPArtworkDataSourceURLCache")
_MPMediaControlsPresentationController = _Class(
    "_MPMediaControlsPresentationController"
)
MPHomeSharingURLProtocol = _Class("MPHomeSharingURLProtocol")
MPActivityGestureRecognizer = _Class("MPActivityGestureRecognizer")
MPTapGestureRecognizer = _Class("MPTapGestureRecognizer")
MPSwipeGestureRecognizer = _Class("MPSwipeGestureRecognizer")
QueryCriteriaResultsCache = _Class("QueryCriteriaResultsCache")
MPArtworkResizeOperation = _Class("MPArtworkResizeOperation")
MPStoreRedownloadProductOperation = _Class("MPStoreRedownloadProductOperation")
MPAsyncOperation = _Class("MPAsyncOperation")
_MPModelLibraryKeepLocalChangeRequestUpdateItemOperation = _Class(
    "_MPModelLibraryKeepLocalChangeRequestUpdateItemOperation"
)
MPModelLibraryKeepLocalChangeRequestOperation = _Class(
    "MPModelLibraryKeepLocalChangeRequestOperation"
)
MPAsyncBlockOperation = _Class("MPAsyncBlockOperation")
MPModelLibraryStoreIDsImportChangeRequestOperation = _Class(
    "MPModelLibraryStoreIDsImportChangeRequestOperation"
)
MPStoreSocialRequestOperation = _Class("MPStoreSocialRequestOperation")
MPStoreLibraryMappingRequestOperation = _Class("MPStoreLibraryMappingRequestOperation")
MPModelLibraryHasPurchasesRequestOperation = _Class(
    "MPModelLibraryHasPurchasesRequestOperation"
)
MPModelLibraryPlaylistEditChangeRequestOperation = _Class(
    "MPModelLibraryPlaylistEditChangeRequestOperation"
)
_MPStoreLibraryPersonalizationAggregateLibraryAddedOperation = _Class(
    "_MPStoreLibraryPersonalizationAggregateLibraryAddedOperation"
)
MPStoreLibraryPersonalizationRequestOperation = _Class(
    "MPStoreLibraryPersonalizationRequestOperation"
)
MPModelLibraryAddToPlaylistChangeRequestOperation = _Class(
    "MPModelLibraryAddToPlaylistChangeRequestOperation"
)
MPModelPlaylistEntriesShareEligibilityRequestOperation = _Class(
    "MPModelPlaylistEntriesShareEligibilityRequestOperation"
)
MPModelLibrarySearchRequestOperation = _Class("MPModelLibrarySearchRequestOperation")
MPStoreLyricsRequestOperation = _Class("MPStoreLyricsRequestOperation")
MPModelLibraryKeepLocalStatusRequestOperation = _Class(
    "MPModelLibraryKeepLocalStatusRequestOperation"
)
MPModelLibraryImportChangeRequestOperation = _Class(
    "MPModelLibraryImportChangeRequestOperation"
)
MPModelLibraryGlobalPlaylistImportChangeRequestOperation = _Class(
    "MPModelLibraryGlobalPlaylistImportChangeRequestOperation"
)
MPRTCReportingPrepareInternalSessionOperation = _Class(
    "MPRTCReportingPrepareInternalSessionOperation"
)
_MPModelShimRequestMiddlewareOperation = _Class(
    "_MPModelShimRequestMiddlewareOperation"
)
MPModelLibraryAlbumAppDataChangeRequestOperation = _Class(
    "MPModelLibraryAlbumAppDataChangeRequestOperation"
)
_MPModelLibraryRequestItemsQueryOperation = _Class(
    "_MPModelLibraryRequestItemsQueryOperation"
)
MPModelLibraryRequestOperation = _Class("MPModelLibraryRequestOperation")
MPModelLibraryDeleteEntityChangeRequestOperation = _Class(
    "MPModelLibraryDeleteEntityChangeRequestOperation"
)
MPStoreModelRequestOperation = _Class("MPStoreModelRequestOperation")
MPModelStoreBrowseRoomMusicKitRequestOperation = _Class(
    "MPModelStoreBrowseRoomMusicKitRequestOperation"
)
MPModelRecentlyPlayedRequestOperation = _Class("MPModelRecentlyPlayedRequestOperation")
MPModelStoreBrowseRequestOperation = _Class("MPModelStoreBrowseRequestOperation")
MPModelForYouRecommendationsRequestOperation = _Class(
    "MPModelForYouRecommendationsRequestOperation"
)
MPModelStoreGroupingsMusicKitRequestOperation = _Class(
    "MPModelStoreGroupingsMusicKitRequestOperation"
)
MPModelStoreBrowseMusicKitRequestOperation = _Class(
    "MPModelStoreBrowseMusicKitRequestOperation"
)
MPModelStoreRadioMusicKitRequestOperation = _Class(
    "MPModelStoreRadioMusicKitRequestOperation"
)
MPModelForYouRecommendationsMusicKitRequestOperation = _Class(
    "MPModelForYouRecommendationsMusicKitRequestOperation"
)
MPSectionedIdentifierListReverseEnumerator = _Class(
    "MPSectionedIdentifierListReverseEnumerator"
)
MPSectionedIdentifierListEnumerator = _Class("MPSectionedIdentifierListEnumerator")
MPMultiSortDescriptor = _Class("MPMultiSortDescriptor")
MPModelSortDescriptor = _Class("MPModelSortDescriptor")
MPRouteLabel = _Class("MPRouteLabel")
MPVideoPlaybackBackgroundView = _Class("MPVideoPlaybackBackgroundView")
MPSubtitlesContainerView = _Class("MPSubtitlesContainerView")
MPAdvertisementContainerView = _Class("MPAdvertisementContainerView")
MPVideoContainerView = _Class("MPVideoContainerView")
MPAVRoutingSheet = _Class("MPAVRoutingSheet")
MPVideoOverlay = _Class("MPVideoOverlay")
_MPDownloadProgressRingView = _Class("_MPDownloadProgressRingView")
MPDownloadProgressView = _Class("MPDownloadProgressView")
MPAVRoutingTableHeaderView = _Class("MPAVRoutingTableHeaderView")
MPSwipableView = _Class("MPSwipableView")
MPVolumeView = _Class("MPVolumeView")
MPVideoPlaybackOverlayView = _Class("MPVideoPlaybackOverlayView")
MPVideoView = _Class("MPVideoView")
_MPAVPlayerView = _Class("_MPAVPlayerView")
_MPAVPlayerViewPlayerLayerView = _Class("_MPAVPlayerViewPlayerLayerView")
MPVideoDestinationBackgroundView = _Class("MPVideoDestinationBackgroundView")
MPVideoBackgroundView = _Class("MPVideoBackgroundView")
MPTransportControls = _Class("MPTransportControls")
_MPMoviePlayerProxyView = _Class("_MPMoviePlayerProxyView")
MPMovieTVHUDView = _Class("MPMovieTVHUDView")
MPReflectionImageView = _Class("MPReflectionImageView")
MPAVRoutingTableViewHeaderView = _Class("MPAVRoutingTableViewHeaderView")
MPAVClippingTableView = _Class("MPAVClippingTableView")
MPAVClippingTableViewCell = _Class("MPAVClippingTableViewCell")
MPAVRoutingTableViewCell = _Class("MPAVRoutingTableViewCell")
MPFullscreenWindow = _Class("MPFullscreenWindow")
_MPAVRoutingSheetSecureWindow = _Class("_MPAVRoutingSheetSecureWindow")
MPTVOutWindow = _Class("MPTVOutWindow")
MPModalPresentationWindow = _Class("MPModalPresentationWindow")
MPAddKeepLocalControl = _Class("MPAddKeepLocalControl")
MPRouteButton = _Class("MPRouteButton")
MPDetailSlider = _Class("MPDetailSlider")
MPVolumeSlider = _Class("MPVolumeSlider")
MPButton = _Class("MPButton")
MPKnockoutButton = _Class("MPKnockoutButton")
MPTransportButton = _Class("MPTransportButton")
MPInlineVideoFullscreenViewController = _Class("MPInlineVideoFullscreenViewController")
MPAlternateTracksContainerViewController = _Class(
    "MPAlternateTracksContainerViewController"
)
MPFullScreenTransitionViewController = _Class("MPFullScreenTransitionViewController")
_MPAudioAndSubtitlesController = _Class("_MPAudioAndSubtitlesController")
MPAudioAndSubtitlesController = _Class("MPAudioAndSubtitlesController")
MPAVRoutingViewController = _Class("MPAVRoutingViewController")
MPMoviePlayerViewController = _Class("MPMoviePlayerViewController")
MPVolumeSettingsController = _Class("MPVolumeSettingsController")
MPVolumeViewController = _Class("MPVolumeViewController")
MPViewController = _Class("MPViewController")
MPVideoViewController = _Class("MPVideoViewController")
MPAbstractFullScreenVideoViewController = _Class(
    "MPAbstractFullScreenVideoViewController"
)
MPMediaControlsViewController = _Class("MPMediaControlsViewController")
MPMediaControlsStandaloneViewController = _Class(
    "MPMediaControlsStandaloneViewController"
)
MPMusicMediaPickerRemoteViewController = _Class(
    "MPMusicMediaPickerRemoteViewController"
)
MPMediaPickerController = _Class("MPMediaPickerController")
MPMediaArray = _Class("MPMediaArray")
MPMediaEntityResultSetArray = _Class("MPMediaEntityResultSetArray")
_MPMusicPlayerQueueItemsProxy = _Class("_MPMusicPlayerQueueItemsProxy")
