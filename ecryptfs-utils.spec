%define Werror_cflags %nil

%define libmajor 0
%define libname %mklibname ecryptfs %libmajor
%define libnamedevel %mklibname -d ecryptfs
%define libnamestaticdevel %mklibname -d -s ecryptfs

Summary: An Enterprise-class Cryptographic Filesystem for Linux
Name: ecryptfs-utils
Version: 95
Release: 1
Source0: http://launchpad.net/ecryptfs/trunk/%{version}\/+download/%{name}_%{version}.orig.tar.gz
Patch0: ecryptfs-utils_83-fix-link.patch
License: GPLv2+
Group: System/Kernel and hardware
Url: https://launchpad.net/ecryptfs
BuildRequires: openssl-devel
BuildRequires: libkeyutils-devel
BuildRequires: libgcrypt-devel
BuildRequires: pam-devel
BuildRequires: python-devel
BuildRequires: nss-devel
BuildRequires: intltool
BuildRequires: glib2-devel
Requires: python-%{name} = %{version}

%description
eCryptfs is a POSIX-compliant enterprise-class stacked cryptographic
filesystem for Linux. It is derived from Erez Zadok's Cryptfs, implemented
through the FiST framework for generating stacked filesystems. eCryptfs
extends Cryptfs to provide advanced key management and policy features.
eCryptfs stores cryptographic metadata in the header of each file written,
so that encrypted files can be copied between hosts; the file will be
decryptable with the proper key, and there is no need to keep track of any
additional information aside from what is already in the encrypted file
itself. Think of eCryptfs as a sort of ``gnupgfs.''

eCryptfs is a native Linux filesystem (other popular cryptographic
filesystems for Linux require FUSE or operate via RPC calls). The kernel
module component of eCryptfs is upstream in the Linux kernel.


%package -n pam_ecryptfs
Summary: eCryptfs PAM module
Group: System/Libraries
Requires: %name = %version

%description -n pam_ecryptfs
eCryptfs PAM module to automatically mount a private cryptographic
directory.


%package -n %libname
Summary: eCryptfs library
Group: Development/C

%description -n %libname
eCryptfs library.


%package -n %libnamedevel
Summary: eCryptfs library
Group: Development/C
Requires: %libname = %version
Provides: libecryptfs-devel = %version-%release
Provides: %name-devel = %version-%release

%description -n %libnamedevel
eCryptfs development files.


%package -n %libnamestaticdevel
Summary: eCryptfs library
Group: Development/C
Requires: %libnamedevel = %version
Provides: libecryptfs-static-devel = %version-%release

%description -n %libnamestaticdevel
eCryptfs static library development files.

%package -n python-%{name}
Summary: eCryptfs Python library
Group: Development/C
#Requires: python-devel
#Requires: %libnamedevel = %version
Requires: %name = %version

%description -n python-%{name}
eCryptfs Python library.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x 
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make

%install
%makeinstall_std

# only needed to update-notifier, that is a ubuntu-only thing, afaik
rm -f %{buildroot}/usr/share/ecryptfs-record-passphrase
mkdir %{buildroot}/usr/share/applications/
mv    %{buildroot}/usr/share/%{name}/*desktop %{buildroot}/usr/share/applications/

%files
%_datadir/applications/*desktop
%_docdir/%name/README
%_docdir/%name/ecryptfs-faq.html
%_docdir/%name/*.txt
/sbin/mount.ecryptfs
/sbin/umount.ecryptfs
/sbin/mount.ecryptfs_private
/sbin/umount.ecryptfs_private
%_bindir/ecryptfs-add-passphrase
%_bindir/ecryptfs-insert-wrapped-passphrase-into-keyring
%_bindir/ecryptfs-manager
%_bindir/ecryptfs-verify
%_bindir/ecryptfs-mount-private
%_bindir/ecryptfs-rewrap-passphrase
%_bindir/ecryptfs-setup-private
%_bindir/ecryptfs-stat
%_bindir/ecryptfs-umount-private
%_bindir/ecryptfs-unwrap-passphrase
%_bindir/ecryptfs-wrap-passphrase
%_bindir/ecryptfsd
%_bindir/ecryptfs-setup-swap
%_bindir/ecryptfs-rewrite-file
%_bindir/ecryptfs-recover-private
%_bindir/ecryptfs-migrate-home
%_mandir/man1/ecryptfs-add-passphrase.1.*
%_mandir/man1/ecryptfs-generate-tpm-key.1.*
%_mandir/man1/ecryptfs-insert-wrapped-passphrase-into-keyring.1.*
%_mandir/man1/ecryptfs-mount-private.1.*
%_mandir/man1/ecryptfs-rewrap-passphrase.1.*
%_mandir/man1/ecryptfs-setup-private.1.*
%_mandir/man1/ecryptfs-umount-private.1.*
%_mandir/man1/ecryptfs-unwrap-passphrase.1.*
%_mandir/man1/ecryptfs-wrap-passphrase.1.*
%_mandir/man1/ecryptfs-rewrite-file.1.*
%_mandir/man1/ecryptfs-recover-private.1.*
%_mandir/man1/mount.ecryptfs_private.1.*
%_mandir/man1/umount.ecryptfs_private.1.*
%_mandir/man1/ecryptfs-setup-swap.1.*
%_mandir/man1/ecryptfs-stat.1.*
%_mandir/man7/ecryptfs.7.*
%_mandir/man8/ecryptfs-manager.8.*
%_mandir/man8/ecryptfsd.8.*
%_mandir/man8/mount.ecryptfs.8.*
%_mandir/man8/umount.ecryptfs.8.*
%dir %_datadir/ecryptfs-utils
%_datadir/ecryptfs-utils/ecryptfs-mount-private.txt
%_datadir/ecryptfs-utils/ecryptfs-record-passphrase
%_datadir/ecryptfs-utils/ecryptfs-find
%_datadir/locale/ca/LC_MESSAGES/ecryptfs-utils.mo

%files -n pam_ecryptfs
/%_lib/security/pam_ecryptfs.so
%_mandir/man8/pam_ecryptfs.8.*

%files -n %libname
%_libdir/ecryptfs/libecryptfs_key_mod_openssl.so
%_libdir/ecryptfs/libecryptfs_key_mod_passphrase.so
%_libdir/libecryptfs.so.%libmajor
%_libdir/libecryptfs.so.%libmajor.*

%files -n %libnamedevel
%_includedir/ecryptfs.h
%_libdir/libecryptfs.so
%_libdir/pkgconfig/libecryptfs.pc

%files -n %libnamestaticdevel
%_libdir/libecryptfs.la

%files -n python-%name
%{py_puresitedir}/%{name}/libecryptfs.py
%{py_puresitedir}/%{name}/libecryptfs.pyc
%{py_puresitedir}/%{name}/libecryptfs.pyo
%{py_platsitedir}/ecryptfs-utils/_libecryptfs.*
