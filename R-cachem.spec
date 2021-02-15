#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cachem
Version  : 1.0.4
Release  : 4
URL      : https://cran.r-project.org/src/contrib/cachem_1.0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cachem_1.0.4.tar.gz
Summary  : Cache R Objects with Automatic Pruning
Group    : Development/Tools
License  : MIT
Requires: R-cachem-lib = %{version}-%{release}
Requires: R-fastmap
Requires: R-rlang
BuildRequires : R-fastmap
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
either their total size or the age of the oldest object (or both),
    automatically pruning objects to maintain the constraints.

%package lib
Summary: lib components for the R-cachem package.
Group: Libraries

%description lib
lib components for the R-cachem package.


%prep
%setup -q -c -n cachem
cd %{_builddir}/cachem

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613411388

%install
export SOURCE_DATE_EPOCH=1613411388
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cachem
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cachem
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cachem
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc cachem || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cachem/DESCRIPTION
/usr/lib64/R/library/cachem/INDEX
/usr/lib64/R/library/cachem/LICENSE
/usr/lib64/R/library/cachem/Meta/Rd.rds
/usr/lib64/R/library/cachem/Meta/features.rds
/usr/lib64/R/library/cachem/Meta/hsearch.rds
/usr/lib64/R/library/cachem/Meta/links.rds
/usr/lib64/R/library/cachem/Meta/nsInfo.rds
/usr/lib64/R/library/cachem/Meta/package.rds
/usr/lib64/R/library/cachem/NAMESPACE
/usr/lib64/R/library/cachem/NEWS.md
/usr/lib64/R/library/cachem/R/cachem
/usr/lib64/R/library/cachem/R/cachem.rdb
/usr/lib64/R/library/cachem/R/cachem.rdx
/usr/lib64/R/library/cachem/help/AnIndex
/usr/lib64/R/library/cachem/help/aliases.rds
/usr/lib64/R/library/cachem/help/cachem.rdb
/usr/lib64/R/library/cachem/help/cachem.rdx
/usr/lib64/R/library/cachem/help/paths.rds
/usr/lib64/R/library/cachem/html/00Index.html
/usr/lib64/R/library/cachem/html/R.css
/usr/lib64/R/library/cachem/tests/testthat.R
/usr/lib64/R/library/cachem/tests/testthat/test-cache-disk.R
/usr/lib64/R/library/cachem/tests/testthat/test-cache-mem.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/cachem/libs/cachem.so
