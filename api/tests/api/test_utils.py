import pytest

from deploythedocs.api import models, utils


@pytest.mark.parametrize('paths,docs_root,expected', [
    (['a'], '/docs_root', '/docs_root/a'),
    (['b'], '/another_root', '/another_root/b'),
    (['a', 'b', 'c'], '/docs', '/docs/a/b/c'),
])
def test_get_full_path(paths, docs_root, expected):
    """Check that the path is constructed from the docs_root."""
    assert utils.get_full_path(*paths, docs_root=docs_root) == expected


@pytest.mark.parametrize('docs_root,expected', [
    ('/docs_root', '/docs_root/a/b'),
    ('/another_root', '/another_root/a/b'),
])
def test_get_full_path_falls_back_to_settings_values(settings, docs_root,
                                                     expected):
    """Check that when docs_root is not specified it is read from settings."""
    settings.DOCS_ROOT = docs_root
    assert utils.get_full_path('a', 'b') == expected


def test_try_get_version(tmpdir):
    """Check a Version returned if the correct directory structure exists."""
    tmpdir.ensure('a', 'b', dir=True)

    result = utils.try_get_version('a', 'b', docs_root=tmpdir.strpath)

    assert isinstance(result, models.Version)
    assert result.name == 'a'
    assert result.version == 'b'


def test_try_get_version_when_missing(tmpdir):
    """Check that None is returned if the version directory is missing."""
    tmpdir.ensure('a', dir=True)

    result = utils.try_get_version('a', 'b', docs_root=tmpdir.strpath)

    assert result is None
