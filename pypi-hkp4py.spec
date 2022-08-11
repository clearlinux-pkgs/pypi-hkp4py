#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-hkp4py
Version  : 0.2.3.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/12/8f/cfbf0ec8946dcbacab876a8e82d2f3679527d1974f5739706cbb27a5e311/hkp4py-0.2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/8f/cfbf0ec8946dcbacab876a8e82d2f3679527d1974f5739706cbb27a5e311/hkp4py-0.2.3.1.tar.gz
Summary  : A Library to get Keys from a keyserver specified
Group    : Development/Tools
License  : MIT
Requires: pypi-hkp4py-python = %{version}-%{release}
Requires: pypi-hkp4py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(requests)

%description
A Library to get GPG/PGP keys from a Keyserver.
        This library uses the requests module to get the keys.
        
        ## Tested Python Versions
        
        ### Python 2.7
        
        * 2.7.15
        
        ### Python 3
        
        * 3.7

%package python
Summary: python components for the pypi-hkp4py package.
Group: Default
Requires: pypi-hkp4py-python3 = %{version}-%{release}

%description python
python components for the pypi-hkp4py package.


%package python3
Summary: python3 components for the pypi-hkp4py package.
Group: Default
Requires: python3-core
Provides: pypi(hkp4py)
Requires: pypi(requests)

%description python3
python3 components for the pypi-hkp4py package.


%prep
%setup -q -n hkp4py-0.2.3.1
cd %{_builddir}/hkp4py-0.2.3.1
pushd ..
cp -a hkp4py-0.2.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401591
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
