from aeronpy.driver import media_driver
from hamcrest import *


def test_launch():
    with media_driver.launch() as driver:
        assert_that(driver, is_not(empty()))


def test_embedded_launch():
    with media_driver.launch_embedded() as driver:
        assert_that(driver, is_not(empty()))


def test_create_context():
    context = media_driver.create_context(
        aeron_directory_name='/tmp/aeron',
        driver_timeout_ms=100,
        use_windows_high_res_timer=True,
        warn_if_directory_exists=True,
        dir_delete_on_start=True,
        term_buffer_sparse_file=False,
        perform_storage_checks=True,
        file_page_size=4096,
        timer_interval_ns=100,
        image_liveness_timeout_ns=1000,
        publication_linger_timeout_ns=1000)
    assert_that(context.aeronDirectoryName, is_(equal_to('/tmp/aeron')))
    assert_that(context.driverTimeoutMs(), is_(equal_to(100)))
    assert_that(context.useWindowsHighResTimer(), is_(True))
