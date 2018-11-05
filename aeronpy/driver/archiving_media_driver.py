from contextlib import contextmanager
from jnius import autoclass
from . import media_driver


__ArchivingMediaDriver = autoclass('io.aeron.archive.ArchivingMediaDriver')
__ArchivingMediaDriver.__str__ = lambda self: self.toString()

__ArchiveContext = autoclass('io.aeron.archive.Archive$Context')


@contextmanager
def launch(**kwargs):
    """
    Launch a new archiving media driver with configuration of media drive context and arching context passed
    through property key args.
    :parameters:
    - 'aeron_directory_name':
    - 'driver_timeout_ms':
    - 'use_windows_high_res_timer':
    - 'warn_if_directory_exists':
    - 'dir_delete_on_start'
    - 'term_buffer_sparse_file'
    - 'perform_storage_checks'
    - 'file_page_size'
    - 'timer_interval_ns'
    - 'image_liveness_timeout_ns'
    - 'publication_linger_timeout_ns'
    - 'client_liveness_timeout_ns'
    - 'status_message_timeout_ns'
    - 'counter_free_to_reuse_timeout_ns'
    - 'publication_unblock_timeout_ns'
    - 'publication_connection_timeout_ns'
    - 'spies_simulate_connection'
    - 'publication_term_buffer_length'
    - 'ipc_term_buffer_length'
    - 'initial_window_length'
    - 'mtu_length'
    - 'ipc_mtu_length'
    - 'delete_archive_on_start'
    - 'archive_directory_name'
    - 'control_channel'
    - 'control_stream_id'
    - 'local_control_channel'
    - 'local_control_stream_id'
    - 'control_term_buffer_sparse'
    - 'control_term_buffer_length'
    - 'recording_events_channel'
    - 'recording_events_stream_id'
    - 'max_concurrent_recordings'
    - 'max_concurrent_replays'
    - 'max_catalog_entries'
    :return: Newly created archiving media driver.
    """
    driver_context, kwargs = media_driver.create_context(**kwargs)
    archive_context, kwargs = create_archive_context(**kwargs)
    if kwargs:
        raise KeyError(f'unknown parameters - {kwargs.keys()}')

    driver = __ArchivingMediaDriver.launch(driver_context, archive_context)
    try:
        yield driver
    finally:
        driver.close()


def create_archive_context(**kwargs):
    """
    Creates archive context.
    :parameters:
    - 'delete_archive_on_start'
    - 'archive_directory_name'
    - 'control_channel'
    - 'control_stream_id'
    - 'local_control_channel'
    - 'local_control_stream_id'
    - 'control_term_buffer_sparse'
    - 'control_term_buffer_length'
    - 'recording_events_channel'
    - 'recording_events_stream_id'
    - 'max_concurrent_recordings'
    - 'max_concurrent_replays'
    - 'max_catalog_entries'
    :return: Newly created context and unattended parameters
    """
    context = __ArchiveContext()

    delete_archive_on_start = kwargs.pop('delete_archive_on_start', None)
    if delete_archive_on_start:
        context.deleteArchiveOnStart(delete_archive_on_start)

    archive_directory_name = kwargs.pop('archive_directory_name', None)
    if archive_directory_name:
        context.archiveDirectoryName(archive_directory_name)

    control_channel = kwargs.pop('control_channel', None)
    if control_channel:
        context.controlChannel(control_channel)

    control_stream_id = kwargs.pop('control_stream_id', None)
    if control_stream_id:
        context.controlStreamId(control_stream_id)

    local_control_channel = kwargs.pop('local_control_channel', None)
    if local_control_channel:
        context.localControlChannel(local_control_channel)

    local_control_stream_id = kwargs.pop('local_control_stream_id', None)
    if local_control_channel:
        context.localControlStreamId(local_control_stream_id)

    control_term_buffer_sparse = kwargs.pop('control_term_buffer_sparse', None)
    if control_term_buffer_sparse:
        context.controlTermBufferSparse(control_term_buffer_sparse)

    control_term_buffer_length = kwargs.pop('control_term_buffer_length', None)
    if control_term_buffer_length:
        context.controlTermBufferLength(control_term_buffer_length)

    control_mtu_length = kwargs.pop('control_mtu_length', None)
    if control_mtu_length:
        context.controlMtuLength(control_mtu_length)

    recording_events_channel = kwargs.pop('recording_events_channel', None)
    if recording_events_channel:
        context.recordingEventsChannel(recording_events_channel)

    recording_events_stream_id = kwargs.pop('recording_events_stream_id', None)
    if recording_events_stream_id:
        context.recordingEventsStreamId(recording_events_stream_id)

    max_concurrent_recordings = kwargs.pop('max_concurrent_recordings', None)
    if max_concurrent_recordings:
        context.maxConcurrentRecordings(max_concurrent_recordings)

    max_concurrent_replays = kwargs.pop('max_concurrent_replays', None)
    if max_concurrent_replays:
        context.maxConcurrentReplays(max_concurrent_replays)

    max_catalog_entries = kwargs.pop('max_catalog_entries', None)
    if max_catalog_entries:
        context.maxCatalogEntries(max_catalog_entries)

    return context, kwargs




