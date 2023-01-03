#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pmix
Version  : 4.2.2
Release  : 9
URL      : https://github.com/pmix/pmix/archive/v4.2.2/pmix-4.2.2.tar.gz
Source0  : https://github.com/pmix/pmix/archive/v4.2.2/pmix-4.2.2.tar.gz
Summary  : An extended/exascale implementation of the PMIx Standard
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pmix-bin = %{version}-%{release}
Requires: pmix-data = %{version}-%{release}
Requires: pmix-lib = %{version}-%{release}
Requires: pmix-license = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : flex
BuildRequires : grep
BuildRequires : hwloc-dev
BuildRequires : libevent-dev
BuildRequires : munge-dev
BuildRequires : perl
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-cython
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The Process Management Interface (PMI) has been used for quite some time as a
means of exchanging wireup information needed for interprocess communication. Two
versions (PMI-1 and PMI-2) have been released as part of the MPICH effort. While
PMI-2 demonstrates better scaling properties than its PMI-1 predecessor, attaining
rapid launch and wireup of the roughly 1M processes executing across 100k nodes
expected for exascale operations remains challenging.

PMI Exascale (PMIx) represents an attempt to resolve these questions by providing
an extended version of the PMI standard specifically designed to support clusters
up to and including exascale sizes. The overall objective of the project is to
eliminate some current restrictions that impact scalability, and provide
a reference implementation of the PMIx-server that demonstrates the desired level of
scalability.

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
%setup -q -n openpmix-4.2.2
cd %{_builddir}/openpmix-4.2.2

%build
## build_prepend content
./autogen.pl

## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672764754
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%reconfigure --disable-static --enable-pmi-backward-compatibility \
--with-munge
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1672764754
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pmix
cp %{_builddir}/openpmix-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pmix/c0fb365dcaaae482fe7c3673c97d0e8c6d21636d || :
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/%{name}/
cp -r %{buildroot}/etc/* %{buildroot}/usr/share/defaults/etc/%{name}/

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pattrs
/usr/bin/pevent
/usr/bin/plookup
/usr/bin/pmix_info
/usr/bin/pmixcc
/usr/bin/pps
/usr/bin/pquery

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/pmix/pmix-mca-params.conf
/usr/share/pmix/help-cli.txt
/usr/share/pmix/help-pattrs.txt
/usr/share/pmix/help-pcompress.txt
/usr/share/pmix/help-pevent.txt
/usr/share/pmix/help-pfexec-base.txt
/usr/share/pmix/help-pfexec-linux.txt
/usr/share/pmix/help-ploc.txt
/usr/share/pmix/help-plookup.txt
/usr/share/pmix/help-pmdl.txt
/usr/share/pmix/help-pmix-info.txt
/usr/share/pmix/help-pmix-mca-base.txt
/usr/share/pmix/help-pmix-mca-var.txt
/usr/share/pmix/help-pmix-plog.txt
/usr/share/pmix/help-pmix-psensor-file.txt
/usr/share/pmix/help-pmix-psensor-heartbeat.txt
/usr/share/pmix/help-pmix-runtime.txt
/usr/share/pmix/help-pmix-server.txt
/usr/share/pmix/help-pmix-util.txt
/usr/share/pmix/help-pmixcc.txt
/usr/share/pmix/help-pps.txt
/usr/share/pmix/help-pquery.txt
/usr/share/pmix/help-prm.txt
/usr/share/pmix/help-ptl-base.txt
/usr/share/pmix/pmix-valgrind.supp
/usr/share/pmix/pmixcc-wrapper-data.txt

%files dev
%defattr(-,root,root,-)
/usr/include/pmix.h
/usr/include/pmix/src/class/pmix_bitmap.h
/usr/include/pmix/src/class/pmix_hash_table.h
/usr/include/pmix/src/class/pmix_hotel.h
/usr/include/pmix/src/class/pmix_list.h
/usr/include/pmix/src/class/pmix_object.h
/usr/include/pmix/src/class/pmix_pointer_array.h
/usr/include/pmix/src/class/pmix_ring_buffer.h
/usr/include/pmix/src/class/pmix_value_array.h
/usr/include/pmix/src/client/pmix_client_ops.h
/usr/include/pmix/src/common/pmix_attributes.h
/usr/include/pmix/src/common/pmix_iof.h
/usr/include/pmix/src/event/pmix_event.h
/usr/include/pmix/src/hwloc/pmix_hwloc.h
/usr/include/pmix/src/include/pmix_atomic.h
/usr/include/pmix/src/include/pmix_config.h
/usr/include/pmix/src/include/pmix_config_bottom.h
/usr/include/pmix/src/include/pmix_config_top.h
/usr/include/pmix/src/include/pmix_dictionary.h
/usr/include/pmix/src/include/pmix_frameworks.h
/usr/include/pmix/src/include/pmix_globals.h
/usr/include/pmix/src/include/pmix_hash_string.h
/usr/include/pmix/src/include/pmix_portable_platform.h
/usr/include/pmix/src/include/pmix_portable_platform_real.h
/usr/include/pmix/src/include/pmix_prefetch.h
/usr/include/pmix/src/include/pmix_socket_errno.h
/usr/include/pmix/src/include/pmix_stdint.h
/usr/include/pmix/src/include/pmix_types.h
/usr/include/pmix/src/mca/base/pmix_base.h
/usr/include/pmix/src/mca/base/pmix_mca_base_alias.h
/usr/include/pmix/src/mca/base/pmix_mca_base_component_repository.h
/usr/include/pmix/src/mca/base/pmix_mca_base_framework.h
/usr/include/pmix/src/mca/base/pmix_mca_base_var.h
/usr/include/pmix/src/mca/base/pmix_mca_base_var_enum.h
/usr/include/pmix/src/mca/base/pmix_mca_base_var_group.h
/usr/include/pmix/src/mca/base/pmix_mca_base_vari.h
/usr/include/pmix/src/mca/bfrops/base/base.h
/usr/include/pmix/src/mca/bfrops/bfrops.h
/usr/include/pmix/src/mca/bfrops/bfrops_types.h
/usr/include/pmix/src/mca/common/dstore/dstore_base.h
/usr/include/pmix/src/mca/common/dstore/dstore_common.h
/usr/include/pmix/src/mca/common/dstore/dstore_file.h
/usr/include/pmix/src/mca/common/dstore/dstore_segment.h
/usr/include/pmix/src/mca/gds/base/base.h
/usr/include/pmix/src/mca/gds/gds.h
/usr/include/pmix/src/mca/mca.h
/usr/include/pmix/src/mca/pcompress/base/base.h
/usr/include/pmix/src/mca/pcompress/pcompress.h
/usr/include/pmix/src/mca/pdl/base/base.h
/usr/include/pmix/src/mca/pdl/pdl.h
/usr/include/pmix/src/mca/pfexec/base/base.h
/usr/include/pmix/src/mca/pfexec/pfexec.h
/usr/include/pmix/src/mca/pgpu/base/base.h
/usr/include/pmix/src/mca/pgpu/pgpu.h
/usr/include/pmix/src/mca/pif/base/base.h
/usr/include/pmix/src/mca/pif/pif.h
/usr/include/pmix/src/mca/pinstalldirs/base/base.h
/usr/include/pmix/src/mca/pinstalldirs/pinstalldirs.h
/usr/include/pmix/src/mca/pinstalldirs/pinstalldirs_types.h
/usr/include/pmix/src/mca/plog/base/base.h
/usr/include/pmix/src/mca/plog/plog.h
/usr/include/pmix/src/mca/pmdl/base/base.h
/usr/include/pmix/src/mca/pmdl/pmdl.h
/usr/include/pmix/src/mca/pnet/base/base.h
/usr/include/pmix/src/mca/pnet/pnet.h
/usr/include/pmix/src/mca/preg/base/base.h
/usr/include/pmix/src/mca/preg/preg.h
/usr/include/pmix/src/mca/preg/preg_types.h
/usr/include/pmix/src/mca/prm/base/base.h
/usr/include/pmix/src/mca/prm/prm.h
/usr/include/pmix/src/mca/psec/base/base.h
/usr/include/pmix/src/mca/psec/psec.h
/usr/include/pmix/src/mca/psensor/base/base.h
/usr/include/pmix/src/mca/psensor/psensor.h
/usr/include/pmix/src/mca/pshmem/base/base.h
/usr/include/pmix/src/mca/pshmem/pshmem.h
/usr/include/pmix/src/mca/psquash/base/base.h
/usr/include/pmix/src/mca/psquash/psquash.h
/usr/include/pmix/src/mca/pstat/base/base.h
/usr/include/pmix/src/mca/pstat/pstat.h
/usr/include/pmix/src/mca/pstrg/base/base.h
/usr/include/pmix/src/mca/pstrg/pstrg.h
/usr/include/pmix/src/mca/ptl/base/base.h
/usr/include/pmix/src/mca/ptl/base/ptl_base_handshake.h
/usr/include/pmix/src/mca/ptl/ptl.h
/usr/include/pmix/src/mca/ptl/ptl_types.h
/usr/include/pmix/src/runtime/pmix_init_util.h
/usr/include/pmix/src/runtime/pmix_progress_threads.h
/usr/include/pmix/src/runtime/pmix_rte.h
/usr/include/pmix/src/server/pmix_server_ops.h
/usr/include/pmix/src/threads/pmix_mutex.h
/usr/include/pmix/src/threads/pmix_mutex_unix.h
/usr/include/pmix/src/threads/pmix_threads.h
/usr/include/pmix/src/threads/pmix_tsd.h
/usr/include/pmix/src/tool/pmix_tool_ops.h
/usr/include/pmix/src/util/pmix_alfg.h
/usr/include/pmix/src/util/pmix_argv.h
/usr/include/pmix/src/util/pmix_basename.h
/usr/include/pmix/src/util/pmix_cmd_line.h
/usr/include/pmix/src/util/pmix_context_fns.h
/usr/include/pmix/src/util/pmix_environ.h
/usr/include/pmix/src/util/pmix_error.h
/usr/include/pmix/src/util/pmix_fd.h
/usr/include/pmix/src/util/pmix_few.h
/usr/include/pmix/src/util/pmix_getcwd.h
/usr/include/pmix/src/util/pmix_getid.h
/usr/include/pmix/src/util/pmix_hash.h
/usr/include/pmix/src/util/pmix_if.h
/usr/include/pmix/src/util/pmix_keyval_parse.h
/usr/include/pmix/src/util/pmix_name_fns.h
/usr/include/pmix/src/util/pmix_net.h
/usr/include/pmix/src/util/pmix_os_dirpath.h
/usr/include/pmix/src/util/pmix_os_path.h
/usr/include/pmix/src/util/pmix_output.h
/usr/include/pmix/src/util/pmix_parse_options.h
/usr/include/pmix/src/util/pmix_path.h
/usr/include/pmix/src/util/pmix_printf.h
/usr/include/pmix/src/util/pmix_pty.h
/usr/include/pmix/src/util/pmix_show_help.h
/usr/include/pmix/src/util/pmix_string_copy.h
/usr/include/pmix/src/util/pmix_strnlen.h
/usr/include/pmix/src/util/pmix_timings.h
/usr/include/pmix/src/util/pmix_vmem.h
/usr/include/pmix_common.h
/usr/include/pmix_deprecated.h
/usr/include/pmix_server.h
/usr/include/pmix_tool.h
/usr/include/pmix_version.h
/usr/lib64/pkgconfig/pmix.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpmix.so
/usr/lib64/libpmix.so.2
/usr/lib64/libpmix.so.2.6.2
/usr/lib64/pmix/pmix_mca_pcompress_zlib.so
/usr/lib64/pmix/pmix_mca_prm_default.so
/usr/lib64/pmix/pmix_mca_prm_slurm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pmix/c0fb365dcaaae482fe7c3673c97d0e8c6d21636d
