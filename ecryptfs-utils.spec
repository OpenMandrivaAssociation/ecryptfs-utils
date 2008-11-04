
%define libmajor 0
%define libname %mklibname ecryptfs %libmajor
%define libnamedevel %mklibname -d ecryptfs
%define libnamestaticdevel %mklibname -d -s ecryptfs

Summary: An Enterprise-class Cryptographic Filesystem for Linux
Name: ecryptfs-utils
Version: 61
Release: %mkrel 1
Source0: http://ufpr.dl.sourceforge.net/sourceforge/ecryptfs/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: System/Kernel and hardware
Url: http://ecryptfs.sourceforge.net/
BuildRequires: openssl-devel
BuildRequires: libkeyutils-devel
BuildRequires: libgcrypt-devel
BuildRequires: libpam-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


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


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_docdir/%name/README
%_docdir/%name/ecryptfs-faq.html
%_docdir/%name/ecryptfs-pam-doc.txt
/sbin/mount.ecryptfs
/sbin/mount.ecryptfs_private
/sbin/umount.ecryptfs_private
%_bindir/ecryptfs-add-passphrase
%_bindir/ecryptfs-insert-wrapped-passphrase-into-keyring
%_bindir/ecryptfs-manager
%_bindir/ecryptfs-mount-private
%_bindir/ecryptfs-rewrap-passphrase
%_bindir/ecryptfs-setup-private
%_bindir/ecryptfs-stat
%_bindir/ecryptfs-umount-private
%_bindir/ecryptfs-unwrap-passphrase
%_bindir/ecryptfs-wrap-passphrase
%_bindir/ecryptfs-zombie-kill
%_bindir/ecryptfs-zombie-list
%_bindir/ecryptfsd
%_mandir/man1/ecryptfs-add-passphrase.1.*
%_mandir/man1/ecryptfs-generate-tpm-key.1.*
%_mandir/man1/ecryptfs-insert-wrapped-passphrase-into-keyring.1.*
%_mandir/man1/ecryptfs-mount-private.1.*
%_mandir/man1/ecryptfs-rewrap-passphrase.1.*
%_mandir/man1/ecryptfs-setup-private.1.*
%_mandir/man1/ecryptfs-umount-private.1.*
%_mandir/man1/ecryptfs-unwrap-passphrase.1.*
%_mandir/man1/ecryptfs-wrap-passphrase.1.*
%_mandir/man1/ecryptfs-zombie-kill.1.*
%_mandir/man1/ecryptfs-zombie-list.1.*
%_mandir/man1/mount.ecryptfs_private.1.*
%_mandir/man1/umount.ecryptfs_private.1.*
%_mandir/man7/ecryptfs.7.*
%_mandir/man8/ecryptfs-manager.8.*
%_mandir/man8/ecryptfsd.8.*
%_mandir/man8/mount.ecryptfs.8.*

%files -n pam_ecryptfs
%defattr(-,root,root)
/%_lib/security/pam_ecryptfs.so
%_mandir/man8/pam_ecryptfs.8.*

%files -n %libname
%_libdir/ecryptfs/libecryptfs_key_mod_openssl.so
%_libdir/ecryptfs/libecryptfs_key_mod_passphrase.so
%_libdir/libecryptfs.so.%libmajor
%_libdir/libecryptfs.so.%libmajor.*

%files -n %libnamedevel
%defattr(-,root,root)
%_includedir/ecryptfs.h
%_libdir/libecryptfs.so
%_libdir/pkgconfig/libecryptfs.pc

%files -n %libnamestaticdevel
%defattr(-,root,root)
%_libdir/libecryptfs.a
%_libdir/libecryptfs.la
