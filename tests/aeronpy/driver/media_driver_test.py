from hamcrest import *
from pytest import fixture, mark
from tempfile import mkdtemp

from aeronpy.driver import media_driver


@fixture()
def custom_aeron_dir():
    return mkdtemp(prefix='aeron_driver')


@mark.skip(reason="disabled temporarily")
def test_launch__default():
    with media_driver.launch() as driver:
        assert_that(driver, is_not(empty()))


def test_launch__customised(custom_aeron_dir):
    with media_driver.launch(aeron_directory_name=custom_aeron_dir) as driver:
        assert_that(driver, is_not(empty()))


def test_launch__unknown_arg():
    def launch(**kwargs):
        with media_driver.launch(**kwargs):
            pass

    assert_that(calling(launch).with_args(unknown_arg='abc'), raises(Exception))


def test_embedded_launch():
    with media_driver.launch_embedded() as driver:
        assert_that(driver, is_not(empty()))


def test_launch_embedded__unknown_arg():
    def launch_embedded(**kwargs):
        with media_driver.launch_embedded(**kwargs):
            pass

    assert_that(calling(launch_embedded).with_args(unknown_arg='abc'), raises(Exception))


def test_create_context__default():
    context, unattended_args = media_driver.create_context()
    assert_that(context, is_not(None))
    assert_that(unattended_args, is_(empty()))


def test_create_context__customised():
    context, unattended_args = media_driver.create_context(
        aeron_directory_name='/tmp/aeron',
        driver_timeout_ms=101,
        use_windows_high_res_timer=True,
        warn_if_directory_exists=True,
        dir_delete_on_start=True,
        term_buffer_sparse_file=False,
        perform_storage_checks=True,
        file_page_size=4096,
        timer_interval_ns=102,
        image_liveness_timeout_ns=1003,
        publication_linger_timeout_ns=1004)
    assert_that(context.aeronDirectoryName, is_(equal_to('/tmp/aeron')))
    assert_that(context.driverTimeoutMs(), is_(equal_to(101)))
    assert_that(context.useWindowsHighResTimer(), is_(True))
    assert_that(context.warnIfDirectoryExists(), is_(True))
    assert_that(context.dirDeleteOnStart(), is_(True))
    assert_that(context.termBufferSparseFile(), is_(False))
    assert_that(context.performStorageChecks(), is_(True))
    assert_that(context.filePageSize(), is_(equal_to(4096)))
    assert_that(context.timerIntervalNs(), is_(equal_to(102)))
    assert_that(context.imageLivenessTimeoutNs(), is_(equal_to(1003)))
    assert_that(context.publicationLingerTimeoutNs(), is_(equal_to(1004)))

    assert_that(unattended_args, is_(empty()))


def test_create_context__wrong_arg_type():
    assert_that(calling(media_driver.create_context).with_args(aeron_directory_name=10), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(driver_timeout_ms='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(use_windows_high_res_timer='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(warn_if_directory_exists='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(dir_delete_on_start='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(term_buffer_sparse_file='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(perform_storage_checks='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(perform_storage_checks='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(file_page_size='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(timer_interval_ns='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(image_liveness_timeout_ns='abc'), raises(Exception))
    assert_that(calling(media_driver.create_context).with_args(publication_linger_timeout_ns='abc'), raises(Exception))


def test_create_context__unattended_args():
    _, unattended_args = media_driver.create_context(unknown_arg='abc')
    assert_that(unattended_args, is_not(empty()))
    assert_that(unattended_args, has_key('unknown_arg'))
