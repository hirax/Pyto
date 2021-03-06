"""
Classes from the 'FileProvider' framework.
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


FPFrameworkOverridesIterator = _Class("FPFrameworkOverridesIterator")
FPItemToURLResourcesConverter = _Class("FPItemToURLResourcesConverter")
FPNSFileProviderItemHelper = _Class("FPNSFileProviderItemHelper")
FPSearchQueryEnumerator = _Class("FPSearchQueryEnumerator")
FPLocalizableStringLookup = _Class("FPLocalizableStringLookup")
FPStringFormat = _Class("FPStringFormat")
FPCTLTermDumper = _Class("FPCTLTermDumper")
FPXEnumeratorAlternateContentsItem = _Class("FPXEnumeratorAlternateContentsItem")
FPExtension_subsystem = _Class("FPExtension_subsystem")
FPItemHierarchyLookup = _Class("FPItemHierarchyLookup")
FPBlockRecoveryAttempter = _Class("FPBlockRecoveryAttempter")
FPItemManager = _Class("FPItemManager")
FPReachabilityMonitor = _Class("FPReachabilityMonitor")
FPXDomainContext = _Class("FPXDomainContext")
FPMaterializedSetEnumerator = _Class("FPMaterializedSetEnumerator")
_FPFilePresenterObserver = _Class("_FPFilePresenterObserver")
NSFileProviderManager = _Class("NSFileProviderManager")
FPAppRegistry = _Class("FPAppRegistry")
FPSpotlightCollectorManager = _Class("FPSpotlightCollectorManager")
FPPersistentStringSet = _Class("FPPersistentStringSet")
FPXPCAutomaticErrorProxy = _Class("FPXPCAutomaticErrorProxy")
FPTask = _Class("FPTask")
FPXIndexState = _Class("FPXIndexState")
FPSearchQueryDataSource = _Class("FPSearchQueryDataSource")
NSFileProviderSearchQuery = _Class("NSFileProviderSearchQuery")
FPStitchingSession = _Class("FPStitchingSession")
FPStitchingManager = _Class("FPStitchingManager")
FPDaemonOperationManager = _Class("FPDaemonOperationManager")
FPExtensionDataSource = _Class("FPExtensionDataSource")
FPArchiveService = _Class("FPArchiveService")
FPArchivedItemDescriptor = _Class("FPArchivedItemDescriptor")
FPAccessControlManager = _Class("FPAccessControlManager")
_FPAccessControlDataSource = _Class("_FPAccessControlDataSource")
FPItemFlags = _Class("FPItemFlags")
_CSSearchableItemAdapter = _Class("_CSSearchableItemAdapter")
FPProviderMonitor = _Class("FPProviderMonitor")
_FPItemList = _Class("_FPItemList")
_FPCopyFileStatus = _Class("_FPCopyFileStatus")
FPPair = _Class("FPPair")
FPLocalization = _Class("FPLocalization")
FPXPCSanitizer = _Class("FPXPCSanitizer")
_FPUnionDataSource = _Class("_FPUnionDataSource")
FPPacer = _Class("FPPacer")
FPPreflightUserInteraction = _Class("FPPreflightUserInteraction")
FPPreflightUserInteractionAlert = _Class("FPPreflightUserInteractionAlert")
FPSpotlightQueryDescriptor = _Class("FPSpotlightQueryDescriptor")
FPAllItemsDescriptor = _Class("FPAllItemsDescriptor")
FPNonEvictableItemsQueryDescriptor = _Class("FPNonEvictableItemsQueryDescriptor")
FPEvictableItemsQueryDescriptor = _Class("FPEvictableItemsQueryDescriptor")
FPFavoriteFoldersQueryDescriptor = _Class("FPFavoriteFoldersQueryDescriptor")
FPTrashedItemsQueryDescriptor = _Class("FPTrashedItemsQueryDescriptor")
FPSearchQueryDescriptor = _Class("FPSearchQueryDescriptor")
FPSharedDocumentsQueryDescriptor = _Class("FPSharedDocumentsQueryDescriptor")
FPTaggedItemsQueryDescriptor = _Class("FPTaggedItemsQueryDescriptor")
FPRecentDocumentsQueryDescriptor = _Class("FPRecentDocumentsQueryDescriptor")
FPXEnumerator = _Class("FPXEnumerator")
FPXObserver = _Class("FPXObserver")
FPXItemsObserver = _Class("FPXItemsObserver")
FPXChangesObserver = _Class("FPXChangesObserver")
FPGracePeriodTimer = _Class("FPGracePeriodTimer")
FPTag = _Class("FPTag")
FPThreadedCopier = _Class("FPThreadedCopier")
FPService = _Class("FPService")
FPSpotlightDataSource = _Class("FPSpotlightDataSource")
FPArchiveTemporaryFolder = _Class("FPArchiveTemporaryFolder")
FPSpotlightCollector = _Class("FPSpotlightCollector")
_FPItemDecorationFallbackLookup = _Class("_FPItemDecorationFallbackLookup")
_FPItemDecorationValueResolver = _Class("_FPItemDecorationValueResolver")
FPItemDecoration = _Class("FPItemDecoration")
FPItemCollectionDiffs = _Class("FPItemCollectionDiffs")
FPItemCollectionItemIDBasedDiffs = _Class("FPItemCollectionItemIDBasedDiffs")
FPItemCollectionIndexPathBasedDiffs = _Class("FPItemCollectionIndexPathBasedDiffs")
FPXSpotlightIndexer = _Class("FPXSpotlightIndexer")
FPItemCollection = _Class("FPItemCollection")
_FPAccessControlCollection = _Class("_FPAccessControlCollection")
FPUnionCollection = _Class("FPUnionCollection")
FPSearchTrashCollection = _Class("FPSearchTrashCollection")
FPTrashUnionCollection = _Class("FPTrashUnionCollection")
FPQueryCollection = _Class("FPQueryCollection")
FPSearchCollection = _Class("FPSearchCollection")
FPExtensionCollection = _Class("FPExtensionCollection")
FPFileManagerFixPermDelegate = _Class("FPFileManagerFixPermDelegate")
FPProgressManager = _Class("FPProgressManager")
FPXServiceEndpointFactory = _Class("FPXServiceEndpointFactory")
FPXXPCListenerDelegate = _Class("FPXXPCListenerDelegate")
FPProviderDomainChangesReceiver = _Class("FPProviderDomainChangesReceiver")
_FPProviderDomainChangesHandlerWrapper = _Class(
    "_FPProviderDomainChangesHandlerWrapper"
)
NSFileProviderExtension = _Class("NSFileProviderExtension")
NSFileProviderInPlaceExtension = _Class("NSFileProviderInPlaceExtension")
FPSearchableItemVersion = _Class("FPSearchableItemVersion")
FPSearchableItemError = _Class("FPSearchableItemError")
FPSearchableItemValue = _Class("FPSearchableItemValue")
FPXExtensionContext = _Class("FPXExtensionContext")
_NSFileProviderExtensionContext = _Class("_NSFileProviderExtensionContext")
FPAppMetadata = _Class("FPAppMetadata")
FPActionOperationLocator = _Class("FPActionOperationLocator")
FPItemOperationLocator = _Class("FPItemOperationLocator")
FPURLOperationLocator = _Class("FPURLOperationLocator")
NSFileProviderItemVersion = _Class("NSFileProviderItemVersion")
_NSFileProviderEmptyItemVersion = _Class("_NSFileProviderEmptyItemVersion")
NSFileProviderRequest = _Class("NSFileProviderRequest")
FPEnumerationSettings = _Class("FPEnumerationSettings")
NSFileProviderEnumerationProperties = _Class("NSFileProviderEnumerationProperties")
FPQueryEnumerationSettings = _Class("FPQueryEnumerationSettings")
FPExtensionEnumerationSettings = _Class("FPExtensionEnumerationSettings")
FPProviderDomain = _Class("FPProviderDomain")
FPProvider = _Class("FPProvider")
FPActionOperationInfo = _Class("FPActionOperationInfo")
FPMoveInfo = _Class("FPMoveInfo")
FPDownloadInfo = _Class("FPDownloadInfo")
FPItem = _Class("FPItem")
NSFileProviderDomain = _Class("NSFileProviderDomain")
FPItemID = _Class("FPItemID")
FPDaemonConnection = _Class("FPDaemonConnection")
FPSandboxingURLWrapper = _Class("FPSandboxingURLWrapper")
FPProgress = _Class("FPProgress")
FPProgressProxy = _Class("FPProgressProxy")
FPAggregateProgress = _Class("FPAggregateProgress")
_FPParentProgress = _Class("_FPParentProgress")
FPOperation = _Class("FPOperation")
FPXIndexOneBatchOperation = _Class("FPXIndexOneBatchOperation")
FPXFetchOneBatchFromWorkingSetOperation = _Class(
    "FPXFetchOneBatchFromWorkingSetOperation"
)
FPXFetchClientStateOperation = _Class("FPXFetchClientStateOperation")
FPXDropSpotlightIndexOperation = _Class("FPXDropSpotlightIndexOperation")
FPActionOperation = _Class("FPActionOperation")
FPVendorDefinedActionOperation = _Class("FPVendorDefinedActionOperation")
FPDisconnectDomainOperation = _Class("FPDisconnectDomainOperation")
FPTransformOperation = _Class("FPTransformOperation")
FPSetFlagsOperation = _Class("FPSetFlagsOperation")
FPSetLastOpenDateOperation = _Class("FPSetLastOpenDateOperation")
FPModifyFavoritesOperation = _Class("FPModifyFavoritesOperation")
FPUntrashOperation = _Class("FPUntrashOperation")
FPTrashOperation = _Class("FPTrashOperation")
FPSetTagsOperation = _Class("FPSetTagsOperation")
FPFetchDefaultContainerOperation = _Class("FPFetchDefaultContainerOperation")
FPEvictOperation = _Class("FPEvictOperation")
FPUnpinOperation = _Class("FPUnpinOperation")
FPPinOperation = _Class("FPPinOperation")
FPDeleteOperation = _Class("FPDeleteOperation")
FPCreateFolderOperation = _Class("FPCreateFolderOperation")
FPRenameOperation = _Class("FPRenameOperation")
FPEmptyAllTrashedItemsOperation = _Class("FPEmptyAllTrashedItemsOperation")
FPWakeForURLSessionOperation = _Class("FPWakeForURLSessionOperation")
FPMoveOperation = _Class("FPMoveOperation")
FPTransferOperation = _Class("FPTransferOperation")
FPCopyOperation = _Class("FPCopyOperation")
FPDownloadOperation = _Class("FPDownloadOperation")
FPFetchPublishingURLOperation = _Class("FPFetchPublishingURLOperation")
FPUnarchiveOperation = _Class("FPUnarchiveOperation")
FPArchiveOperation = _Class("FPArchiveOperation")
FPFetchThumbnailsOperation = _Class("FPFetchThumbnailsOperation")
FPFetchRegularItemThumbnailsOperation = _Class("FPFetchRegularItemThumbnailsOperation")
FPFetchAppLibraryIconsOperation = _Class("FPFetchAppLibraryIconsOperation")
FPError = _Class("FPError")
_FPPageSortedByName = _Class("_FPPageSortedByName")
_FPPageSortedByDate = _Class("_FPPageSortedByDate")
