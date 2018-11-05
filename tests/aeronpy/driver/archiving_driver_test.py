from aeronpy.driver import archiving_media_driver
from hamcrest import *
from pytest import fixture, mark
from tempfile import mkdtemp


@fixture()
def custom_aeron_dir():
    return mkdtemp(prefix='aeron_driver')


@mark.skip(reason="disabled temporarily")
def test_launch__default():
    with archiving_media_driver.launch() as driver:
        assert_that(driver, is_not(None))


def test_launch__customised(custom_aeron_dir):
    with archiving_media_driver.launch(aeron_directory_name=custom_aeron_dir) as driver:
        assert_that(driver, is_not(None))


def test_launch__unknown_arg():
    def launch(**kwargs):
        with archiving_media_driver.launch(**kwargs):
            pass

    assert_that(calling(launch).with_args(unknown_arg='abc'), raises(Exception))


def test_create_archive_context__default():
    context, unattended_args = archiving_media_driver.create_archive_context()
    assert_that(context, is_not(None))
    assert_that(unattended_args, is_(empty()))


def test_create_archive_context__customised():
    context, unattended_args = archiving_media_driver.create_archive_context(
        delete_archive_on_start=True,
        archive_directory_name='abc',
        control_channel='aeron:udp?localhost:1500',
        control_stream_id=1501,
        local_control_channel='aeron:udp?localhost:1502',
        local_control_stream_id=1503,
        control_term_buffer_sparse=True,
        control_term_buffer_length=1504,
        control_mtu_length=1505,
        recording_events_channel='aeron:udp?localhost:1506',
        recording_events_stream_id=1507,
        max_concurrent_recordings=1511,
        max_concurrent_replays=1512,
        max_catalog_entries=1513)

    assert_that(context, is_not(None))
    assert_that(context.deleteArchiveOnStart(), is_(True))
    assert_that(context.archiveDirectoryName(), is_(equal_to('abc')))
    assert_that(context.controlChannel(), is_(equal_to('aeron:udp?localhost:1500')))
    assert_that(context.controlStreamId(), is_(equal_to(1501)))
    assert_that(context.localControlChannel(), is_(equal_to('aeron:udp?localhost:1502')))
    assert_that(context.localControlStreamId(), is_(equal_to(1503)))
    assert_that(context.controlTermBufferSparse(), is_(True))
    assert_that(context.controlTermBufferLength(), is_(equal_to(1504)))
    assert_that(context.controlMtuLength(), is_(equal_to(1505)))
    assert_that(context.recordingEventsChannel(), is_(equal_to('aeron:udp?localhost:1506')))
    assert_that(context.recordingEventsStreamId(), is_(equal_to(1507)))
    assert_that(context.maxConcurrentRecordings(), is_(equal_to(1511)))
    assert_that(context.maxConcurrentReplays(), is_(equal_to(1512)))
    assert_that(context.maxCatalogEntries(), is_(equal_to(1513)))

    assert_that(unattended_args, is_(empty()))


def test_create_archive_context__unattended_args():
    _, unattended_args = archiving_media_driver.create_archive_context(unknown_arg='abc')
    assert_that(unattended_args, is_not(empty()))
    assert_that(unattended_args, has_key('unknown_arg'))
