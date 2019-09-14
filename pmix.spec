#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pmix
Version  : 3.1.4
Release  : 2
URL      : https://github.com/pmix/pmix/archive/v3.1.4/pmix-3.1.4.tar.gz
Source0  : https://github.com/pmix/pmix/archive/v3.1.4/pmix-3.1.4.tar.gz
Summary  : An extended/exascale implementation of PMI
Group    : Development/Tools
License  : Intel
Requires: pmix-bin = %{version}-%{release}
Requires: pmix-data = %{version}-%{release}
Requires: pmix-lib = %{version}-%{release}
Requires: pmix-license = %{version}-%{release}
BuildRequires : Cython
BuildRequires : flex
BuildRequires : hwloc-dev
BuildRequires : libevent-dev
BuildRequires : perl
BuildRequires : pkgconfig(zlib)

%description
The Process Management Interface (PMI) has been used for quite some time as a
means of exchanging wireup information needed for interprocess communication. Two
versions (PMI-1 and PMI-2) have been released as part of the MPICH effort. While
PMI-2 demonstrates better scaling properties than its PMI-1 predecessor, attaining
rapid launch and wireup of the roughly 1M processes executing across 100k nodes
expected for exascale operations remains challenging.

PMI Exascale (PMIx) represents an attempt to resolve these questions by providing
an extended version of the PMI standard specifically designed to support clusters
up to and including exascale sizes. The overall objective of the project is not to
branch the existing pseudo-standard definitions - in fact, PMIx fully supports both
of the existing PMI-1 and PMI-2 APIs - but rather to (a) augment and extend those
APIs to eliminate some current restrictions that impact scalability, and (b) provide
a reference implementation of the PMI-server that demonstrates the desired level of
scalability.

This RPM contains all the tools necessary to compile and link against PMIx.

%package bin
Summary: bin components for the pmix package.
Group: Binaries
Requires: pmix-data = %{version}-%{release}
Requires: pmix-license = %{version}-%{release}

%description bin
bin components for the pmix package.


%package data
Summary: data components for the pmix package.
Group: Data

%description data
data components for the pmix package.


%package dev
Summary: dev components for the pmix package.
Group: Development
Requires: pmix-lib = %{version}-%{release}
Requires: pmix-bin = %{version}-%{release}
Requires: pmix-data = %{version}-%{release}
Provides: pmix-devel = %{version}-%{release}
Requires: pmix = %{version}-%{release}

%description dev
dev components for the pmix package.


%package lib
Summary: lib components for the pmix package.
Group: Libraries
Requires: pmix-data = %{version}-%{release}
Requires: pmix-license = %{version}-%{release}

%description lib
lib components for the pmix package.


%package license
Summary: license components for the pmix package.
Group: Default

%description license
license components for the pmix package.


%prep
%setup -q -n pmix-3.1.4

%build
## build_prepend content
./autogen.pl
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568042572
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --enable-pmi-backward-compatibility
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568042572
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pmix
cp LICENSE %{buildroot}/usr/share/package-licenses/pmix/LICENSE
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/%{name}/
cp -r %{buildroot}/etc/* %{buildroot}/usr/share/defaults/etc/%{name}/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pevent
/usr/bin/plookup
/usr/bin/pmix_info
/usr/bin/pps

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/pmix/pmix-mca-params.conf
/usr/share/pmix/help-pevent.txt
/usr/share/pmix/help-plookup.txt
/usr/share/pmix/help-pmix-info.txt
/usr/share/pmix/help-pmix-mca-base.txt
/usr/share/pmix/help-pmix-mca-var.txt
/usr/share/pmix/help-pmix-plog.txt
/usr/share/pmix/help-pmix-psensor-file.txt
/usr/share/pmix/help-pmix-psensor-heartbeat.txt
/usr/share/pmix/help-pmix-runtime.txt
/usr/share/pmix/help-pmix-server.txt
/usr/share/pmix/help-pps.txt
/usr/share/pmix/pmix-valgrind.supp

%files dev
%defattr(-,root,root,-)
/usr/include/pmi.h
/usr/include/pmi2.h
/usr/include/pmix.h
/usr/include/pmix_common.h
/usr/include/pmix_extend.h
/usr/include/pmix_rename.h
/usr/include/pmix_server.h
/usr/include/pmix_tool.h
/usr/include/pmix_version.h
/usr/lib64/libmca_common_dstore.so
/usr/lib64/libpmi.so
/usr/lib64/libpmi2.so
/usr/lib64/libpmix.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmca_common_dstore.so.1
/usr/lib64/libmca_common_dstore.so.1.0.1
/usr/lib64/libpmi.so.1
/usr/lib64/libpmi.so.1.0.1
/usr/lib64/libpmi2.so.1
/usr/lib64/libpmi2.so.1.0.0
/usr/lib64/libpmix.so.2
/usr/lib64/libpmix.so.2.2.24
/usr/lib64/pmix/mca_bfrops_v12.so
/usr/lib64/pmix/mca_bfrops_v20.so
/usr/lib64/pmix/mca_bfrops_v21.so
/usr/lib64/pmix/mca_bfrops_v3.so
/usr/lib64/pmix/mca_gds_ds12.so
/usr/lib64/pmix/mca_gds_ds21.so
/usr/lib64/pmix/mca_gds_hash.so
/usr/lib64/pmix/mca_plog_default.so
/usr/lib64/pmix/mca_plog_stdfd.so
/usr/lib64/pmix/mca_plog_syslog.so
/usr/lib64/pmix/mca_pnet_tcp.so
/usr/lib64/pmix/mca_pnet_test.so
/usr/lib64/pmix/mca_preg_native.so
/usr/lib64/pmix/mca_psec_native.so
/usr/lib64/pmix/mca_psec_none.so
/usr/lib64/pmix/mca_psensor_file.so
/usr/lib64/pmix/mca_psensor_heartbeat.so
/usr/lib64/pmix/mca_pshmem_mmap.so
/usr/lib64/pmix/mca_ptl_tcp.so
/usr/lib64/pmix/mca_ptl_usock.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pmix/LICENSE
