pkgname = "kdepim-runtime"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-j1", "-E", "(akonadi-sqlite-.*)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "akonadi-notes-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcmutils-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kdav-devel",
    "kidentitymanagement-devel",
    "kimap-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kldap-devel",
    "kmailtransport-devel",
    "kmbox-devel",
    "kmime-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "libkgapi-devel",
    "libsasl-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtspeech-devel",
    "qt6-qtwebengine-devel",
    "qtkeychain-devel",
    "shared-mime-info",
]
depends = ["shared-mime-info"]
checkdepends = ["xwayland-run"] + depends
pkgdesc = "KDE PIM Akonadi agents and runtime resources"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND GPL-2.0-or-later"
url = "https://invent.kde.org/pim/kdepim-runtime"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdepim-runtime-{pkgver}.tar.xz"
)
sha256 = "f470f2565aa6b3ea9866e59e4a19799470c4a7b9ba0ce41cc388fa8563ddd5cb"
