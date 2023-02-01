#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcbor
Version  : 0.10.2
Release  : 4
URL      : https://github.com/PJK/libcbor/archive/v0.10.2/libcbor-0.10.2.tar.gz
Source0  : https://github.com/PJK/libcbor/archive/v0.10.2/libcbor-0.10.2.tar.gz
Summary  : @PROJECT_NAME@ - CBOR protocol implementation
Group    : Development/Tools
License  : MIT
Requires: libcbor-lib = %{version}-%{release}
Requires: libcbor-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(cmocka)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# [libcbor](https://github.com/PJK/libcbor)
[![CircleCI](https://circleci.com/gh/PJK/libcbor/tree/master.svg?style=svg)](https://circleci.com/gh/PJK/libcbor/tree/master)
[![Build status](https://ci.appveyor.com/api/projects/status/8kkmvmefelsxp5u2?svg=true)](https://ci.appveyor.com/project/PJK/libcbor)
[![Documentation Status](https://readthedocs.org/projects/libcbor/badge/?version=latest)](https://readthedocs.org/projects/libcbor/?badge=latest)
[![latest packaged version(s)](https://repology.org/badge/latest-versions/libcbor.svg)](https://repology.org/project/libcbor/versions)
[![codecov](https://codecov.io/gh/PJK/libcbor/branch/master/graph/badge.svg)](https://codecov.io/gh/PJK/libcbor)

%package dev
Summary: dev components for the libcbor package.
Group: Development
Requires: libcbor-lib = %{version}-%{release}
Provides: libcbor-devel = %{version}-%{release}
Requires: libcbor = %{version}-%{release}

%description dev
dev components for the libcbor package.


%package lib
Summary: lib components for the libcbor package.
Group: Libraries
Requires: libcbor-license = %{version}-%{release}

%description lib
lib components for the libcbor package.


%package license
Summary: license components for the libcbor package.
Group: Default

%description license
license components for the libcbor package.


%prep
%setup -q -n libcbor-0.10.2
cd %{_builddir}/libcbor-0.10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675264632
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1675264632
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcbor
cp %{_builddir}/libcbor-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/libcbor/6d7043cf5c99126e691b25b52b7327ca407978c0 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cbor.h
/usr/include/cbor/arrays.h
/usr/include/cbor/bytestrings.h
/usr/include/cbor/callbacks.h
/usr/include/cbor/cbor_export.h
/usr/include/cbor/common.h
/usr/include/cbor/configuration.h
/usr/include/cbor/data.h
/usr/include/cbor/encoding.h
/usr/include/cbor/floats_ctrls.h
/usr/include/cbor/internal/builder_callbacks.h
/usr/include/cbor/internal/encoders.h
/usr/include/cbor/internal/loaders.h
/usr/include/cbor/internal/memory_utils.h
/usr/include/cbor/internal/stack.h
/usr/include/cbor/internal/unicode.h
/usr/include/cbor/ints.h
/usr/include/cbor/maps.h
/usr/include/cbor/serialization.h
/usr/include/cbor/streaming.h
/usr/include/cbor/strings.h
/usr/include/cbor/tags.h
/usr/lib64/libcbor.so
/usr/lib64/pkgconfig/libcbor.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcbor.so.0.10
/usr/lib64/libcbor.so.0.10.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcbor/6d7043cf5c99126e691b25b52b7327ca407978c0
