import os
from xml.dom import minidom
from os import walk
from functools import reduce


def read_permissions(manifest):
    permissions = []
    xmldoc = minidom.parse(manifest)
    itemlist = xmldoc.getElementsByTagName('uses-permission')
    for s in itemlist:
        if s.attributes['android:name']:
            permission = s.attributes['android:name'].value.split(".")
            permission_name = permission[-1]
            if permission_name.isupper():
                permissions.append(permission_name)
            else:
                # tratando casos especiais. EX: com.amazon.dcp.sso.permission.AmazonAccountPropertyService.property.changed
                permissions.append(permission[-2] + "." + permission_name)
    return permissions


def read_manifests(dir):
    apps = {}
    _, _, filenames = next(walk(dir))
    for file in filenames:
        manifest = os.path.join(dir, file)
        permissions = read_permissions(manifest)
        app_name = file.replace("AndroidManifest_", "")
        app_name = app_name.replace(".xml", "")
        apps[app_name] = permissions
    return apps


def get_intersection(apps):
    intersection = set()
    aux = []
    for app in apps:
        aux.append(apps[app])
    return list(reduce(set.intersection, [set(item) for item in aux]))


def get_difference(app, apps):
    permissoes_app = set(apps[app])
    permissoes_outros_apps = []
    for tmp in apps:
        if app != tmp:
            permissoes_outros_apps.append(apps[tmp])
    return permissoes_app.difference(*permissoes_outros_apps)


# EXECUTAR
if __name__ == "__main__":
    dir = os.path.join(os.path.abspath(os.getcwd()), "manifest")
    apps = read_manifests(dir)

    print("INTERSECÇÃO:", get_intersection(apps))

    print("\n\nDIFERENÇA: ")
    for app in apps:
        diff = get_difference(app, apps)
        print(app, "=", diff)
