from contextlib import contextmanager
from jnius import autoclass, cast
from tempfile import mkdtemp


__MediaDriver = autoclass('io.aeron.driver.MediaDriver')
__MediaDriver.__str__ = lambda self: self.toString()

__System = autoclass('java.lang.System')
__Context = autoclass('io.aeron.driver.MediaDriver$Context')
__CommonContext = autoclass('io.aeron.CommonContext')


@contextmanager
def launch(**kwargs):
    """
    Launch a MediaDriver embedded in the current process with default configuration.
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
    :return: Launched media driver instance.
    """
    context, kwargs = create_context(**kwargs)
    if kwargs:
        raise KeyError(f'unknown parameters - {kwargs.keys()}')

    driver = __MediaDriver.launch(context)
    try:
        yield driver
    finally:
        driver.close()


@contextmanager
def launch_embedded(**kwargs):
    """
    Launch an isolated MediaDriver embedded in the current process with a provided configuration ctx and a generated
    **aeron_directory_name** that can be retrieved by calling `aeronDirectoryName`.
    :parameters:
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
    :return: Launched embedded media driver instance.
    """
    kwargs['aeron_directory_name'] = mkdtemp('aeron_driver')
    context, kwargs = create_context(**kwargs)
    if kwargs:
        raise KeyError(f'unknown parameters - {kwargs.keys()}')

    driver = __MediaDriver.launchEmbedded(context)
    try:
        yield driver
    finally:
        driver.close()


def create_context(**kwargs):
    """
    Creates media driver context.
    :Parameters:
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
    :return: Newly created context and unattended parameters
    """
    # nasty hack caused by limitation of python-java bridge
    aeron_directory_name = kwargs.pop('aeron_directory_name', None)
    if aeron_directory_name:
        __System.setProperty('aeron.dir', aeron_directory_name)

    context = __Context()

    driver_timeout_ms = kwargs.pop('driver_timeout_ms', None)
    if driver_timeout_ms:
        context.driverTimeoutMs(driver_timeout_ms)

    use_windows_high_res_timer = kwargs.pop('use_windows_high_res_timer', None)
    if use_windows_high_res_timer:
        context.useWindowsHighResTimer(use_windows_high_res_timer)

    warn_if_directory_exists = kwargs.pop('warn_if_directory_exists', None)
    if warn_if_directory_exists:
        context.warnIfDirectoryExists(warn_if_directory_exists)

    dir_delete_on_start = kwargs.pop('dir_delete_on_start', None)
    if dir_delete_on_start:
        context.dirDeleteOnStart(dir_delete_on_start)

    term_buffer_sparse_file = kwargs.pop('term_buffer_sparse_file', None)
    if term_buffer_sparse_file:
        context.termBufferSparseFile(term_buffer_sparse_file)

    perform_storage_checks = kwargs.pop('perform_storage_checks', None)
    if perform_storage_checks:
        context.performStorageChecks(perform_storage_checks)

    file_page_size = kwargs.pop('file_page_size', None)
    if file_page_size:
        context.filePageSize(file_page_size)

    timer_interval_ns = kwargs.pop('timer_interval_ns', None)
    if timer_interval_ns:
        context.timerIntervalNs(timer_interval_ns)

    image_liveness_timeout_ns = kwargs.pop('image_liveness_timeout_ns', None)
    if image_liveness_timeout_ns:
        context.imageLivenessTimeoutNs(image_liveness_timeout_ns)

    publication_linger_timeout_ns = kwargs.pop('publication_linger_timeout_ns', None)
    if publication_linger_timeout_ns:
        context.publicationLingerTimeoutNs(publication_linger_timeout_ns)

    client_liveness_timeout_ns = kwargs.pop('client_liveness_timeout_ns', None)
    if client_liveness_timeout_ns:
        context.clientLivenessTimeoutNs(client_liveness_timeout_ns)

    status_message_timeout_ns = kwargs.pop('status_message_timeout_ns', None)
    if status_message_timeout_ns:
        context.statusMessageTimeoutNs(status_message_timeout_ns)

    counter_free_to_reuse_timeout_ns = kwargs.pop('counter_free_to_reuse_timeout_ns', None)
    if counter_free_to_reuse_timeout_ns:
        context.counterFreeToReuseTimeoutNs(counter_free_to_reuse_timeout_ns)

    publication_unblock_timeout_ns = kwargs.pop('publication_unblock_timeout_ns', None)
    if publication_unblock_timeout_ns:
        context.publicationUnblockTimeoutNs(publication_unblock_timeout_ns)

    publication_connection_timeout_ns = kwargs.pop('publication_connection_timeout_ns', None)
    if publication_connection_timeout_ns:
        context.publicationConnectionTimeoutNs(publication_connection_timeout_ns)

    spies_simulate_connection = kwargs.pop('spies_simulate_connection', None)
    if spies_simulate_connection:
        context.spiesSimulateConnection(spies_simulate_connection)

    publication_term_buffer_length = kwargs.pop('publication_term_buffer_length', None)
    if publication_term_buffer_length:
        context.publicationTermBufferLength(publication_term_buffer_length)

    ipc_term_buffer_length = kwargs.pop('ipc_term_buffer_length', None)
    if ipc_term_buffer_length:
        context.ipcTermBufferLength(ipc_term_buffer_length)

    initial_window_length = kwargs.pop('initial_window_length', None)
    if initial_window_length:
        context.initialWindowLength(initial_window_length)

    mtu_length = kwargs.pop('mtu_length', None)
    if mtu_length:
        context.mtuLength(mtu_length)

    ipc_mtu_length = kwargs.pop('ipc_mtu_length', None)
    if ipc_mtu_length:
        context.ipcMtuLength(ipc_mtu_length)

    return context, kwargs


def is_active(aeron_directory_name=None):
    context, _ = create_context(aeron_directory_name=aeron_directory_name)
    context.conclude()

    directory = context.aeronDirectory()
    driver_timeout_ms = context.driverTimeoutMs()
    consumer = cast('java.util.function.Consumer<S>', None)
    return __CommonContext.isDriverActive(directory, driver_timeout_ms, consumer)
