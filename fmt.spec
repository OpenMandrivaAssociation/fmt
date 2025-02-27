%define major %(echo %{version}|cut -d. -f1)
%define libname %mklibname %{name}
%define devel %mklibname -d %{name}

Summary:	Small, safe and fast formatting library
Name:		fmt
Version:	11.1.4
Release:	1
Group:		Development/C++
License:	BSD
URL:		https://fmtlib.org
Source0:	https://github.com/fmtlib/fmt/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	cmake

%description
fmt is an open-source formatting library for C++. It can be used as a safe
alternative to printf or as a fast alternative to IOStreams.

%package -n %{devel}
Summary:	Development files for libfmt
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel

%description -n %{devel}
This package contains the development header files, libraries
and cmake files for libfmt

%package -n %{libname}
Summary:	The libfmt libraries
Group:		Development/C++

%description -n %{libname}
This package contains the library for libfmt

%files -n %{libname}
%{_libdir}/libfmt.so.%{major}*

%files -n %{devel}
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/libfmt.so
%{_libdir}/pkgconfig/%{name}.pc

