import os
import shutil
import zipfile

from django.conf import settings

from deploythedocs.api.models import Version


def get_full_path(*paths, docs_root=None):
    """Join the given paths to the docs_root directory."""
    docs_root = docs_root or settings.DOCS_ROOT
    return os.path.join(docs_root, *paths)


def try_get_version(name, version, docs_root=None):
    """Return a Version if it exists on disk else None."""
    path = get_full_path(name, version, docs_root=docs_root)

    if os.path.exists(path):
        return Version(name=name, version=version)
    return None


def create_or_update(version, docs_root=None):
    """Create or update the files for the given Version."""
    path = get_full_path(version.name, version.version, docs_root=docs_root)
    os.makedirs(path, exist_ok=True)
    zipfile.ZipFile(version.bundle).extractall(path)


def destroy(version, docs_root=None):
    """Remove the files for the given Version.
    
    If we just removed the last Version for a given project then we also remove
    the project directory.
    """
    version_path = get_full_path(version.name, version.version, docs_root=docs_root)
    shutil.rmtree(version_path)

    project_path = get_full_path(version.name, docs_root=docs_root)

    if not os.listdir(project_path):
        shutil.rmtree(project_path)


def list_versions(name, docs_root=None):
    """Return a list of Versions for the given project name."""
    path = get_full_path(name, docs_root=docs_root)

    if os.path.exists(path):
        versions = []

        for version_string in sorted(os.listdir(path), reverse=True):

            version = Version(name=name, version=version_string)
            versions.append(version)

        return versions

    return []


def list_all(docs_root=None):
    """Return a list of projects and their versions."""
    docs_root = get_full_path(docs_root=docs_root)

    projects = []

    for name in sorted(os.listdir(docs_root)):
        path = os.path.join(docs_root, name)
        if os.path.isdir(path):
            projects.append({'name': name, 'versions': list_versions(name)})

    return projects
