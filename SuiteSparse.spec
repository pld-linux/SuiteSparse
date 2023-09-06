# TODO: GPU_CONFIG (CUDA) support, TBB
#
# Conditional build:
%bcond_without	metis		# partition support (using metis lib)

# main package version
%define		suite_ver	5.5.0
# see */Include/*.h /VER(SION)?_CODE, C*Sparse/Include/cs.h /CS_VER
%define		amd_ver		2.4.6
%define		btf_ver		1.2.6
%define		camd_ver	2.4.6
%define		ccolamd_ver	2.9.6
%define		colamd_ver	2.9.6
%define		cholmod_ver	3.0.13
%define		csparse_ver	3.2.0
%define		cxsparse_ver	3.2.0
%define		klu_ver		1.3.9
%define		ldl_ver		2.2.6
%define		rbio_ver	2.2.6
%define		spqr_ver	2.0.9
%define		umfpack_ver	5.7.8
%define		gpuruntime_ver	1.0.5
%define		gpuqrengine_ver	1.0.5
# GraphBLAS version 2.3.5, but disabled here, newer version is built from GraphBLAS.spec
# Mongoose version 2.0.4, but disabled here, the same version is built from SuiteSparse-Mongoose.spec

Summary:	A Suite of Sparse matrix packages
Summary(pl.UTF-8):	Zbiór pakietów do operacji na macierzach rzadkich
Name:		SuiteSparse
Version:	%{suite_ver}
Release:	6
License:	LGPL v2.1+, GPL v2+
Group:		Libraries
#Source0Download: https://github.com/DrTimothyAldenDavis/SuiteSparse/releases
Source0:	https://github.com/DrTimothyAldenDavis/SuiteSparse/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f70d7f9b01622da030dcb226abacd1ad
Patch0:		%{name}-config.patch
Patch1:		%{name}-amdf77.patch
Patch2:		%{name}-externc.patch
Patch3:		%{name}-ILP32.patch
URL:		http://suitesparse.com/
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%if %{with metis}
BuildRequires:	metis-devel >= 5
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Suite of Sparse matrix packages.

%description -l pl.UTF-8
Suite Sparse to zbiór pakietów do operacji na macierzach rzadkich.

%package config
Summary:	SuiteSparse_config development files
Summary(pl.UTF-8):	Pliki programistyczne SuiteSparse_config
License:	no restrictions
Group:		Development
Provides:	SuiteSparse_config = %{suite_ver}-%{release}
Obsoletes:	SuiteSparse_config < 4.4

%description config
SuiteSparse_config is required by nearly all sparse matrix packages
that are authored by Timothy A. Davis.

Before version 4, SuiteSparse_config used to be named UFconfig.

%description config -l pl.UTF-8
SuiteSparse_config jest wymagany przez prawie wszystkie pakiety do
obliczeń na macierzach rzadkich autorstwa Timothy'ego A. Davisa.

SuiteSparse_config przed wersją 4 nazywał się UFconfig.

%package config-libs
Summary:	SuiteSparse_config shared library
Summary(pl.UTF-8):	Biblioteka współdzielona SuiteSparse_config
License:	no restrictions
Group:		Libraries
Provides:	SuiteSparse_config-libs = %{suite_ver}-%{release}
Obsoletes:	SuiteSparse_config-libs < 4.4

%description config-libs
SuiteSparse_config shared library, containing malloc/free wrappers.

%description config-libs -l pl.UTF-8
Biblioteka współdzielona SuiteSparse_config, zawierająca funkcje
obudowujące malloc/free.

%package config-devel
Summary:	Development files for SuiteSparse_config library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki SuiteSparse_config
License:	no restrictions
Group:		Development/Libraries
Requires:	%{name}-config = %{suite_ver}-%{release}
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	SuiteSparse_config-devel = %{suite_ver}-%{release}
Obsoletes:	SuiteSparse_config-devel < 4.4

%description config-devel
Development files for SuiteSparse_config library.

%description config-devel -l pl.UTF-8
Pliki programistyczne biblioteki SuiteSparse_config.

%package config-static
Summary:	SuiteSparse_config static library
Summary(pl.UTF-8):	Biblioteka statyczna SuiteSparse_config
License:	no restrictions
Group:		Libraries
Requires:	%{name}-config-devel = %{suite_ver}-%{release}
Provides:	SuiteSparse_config-static = %{suite_ver}-%{release}
Obsoletes:	SuiteSparse_config-static < 4.4

%description config-static
SuiteSparse_config static library.

%description config-static -l pl.UTF-8
Biblioteka statyczna SuiteSparse_config.

%package AMD
Summary:	AMD: Approximate Minimum Degree
Summary(pl.UTF-8):	AMD - przybliżony algorytm minimalnego stopnia
Version:	%{amd_ver}
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	AMD = %{amd_ver}-%{release}
Obsoletes:	AMD < 2.4.0-5

%description AMD
AMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting). There are versions in both C and Fortran. A MATLAB
interface is provided. Note that this software has nothing to do with
AMD the company.

%description AMD -l pl.UTF-8
AMD to zbiór procedur do porządkowania macierzy rzadkich przed
rozkładem Cholesky'ego (lub do rozkładu LU z obrotami diagonalnymi).
Istnieją wersje zarówno w C, jak i Fortranie. Dostępny jest interfejs
do MATLAB-a. Uwaga: to oprogramowanie nie ma nic wspólnego z firmą
AMD.

%package AMD-devel
Summary:	Header files for AMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AMD
Version:	%{amd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-AMD = %{amd_ver}-%{release}
Requires:	%{name}-config = %{suite_ver}-%{release}
Provides:	AMD-devel = %{amd_ver}-%{release}
Obsoletes:	AMD-devel < 2.4.0-5

%description AMD-devel
Header files for AMD library.

%description AMD-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AMD.

%package AMD-static
Summary:	Static AMD library
Summary(pl.UTF-8):	Statyczna biblioteka AMD
Version:	%{amd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-AMD-devel = %{amd_ver}-%{release}
Provides:	AMD-static = %{amd_ver}-%{release}
Obsoletes:	AMD-static < 2.4.0-5

%description AMD-static
Static AMD library.

%description AMD-static -l pl.UTF-8
Statyczna biblioteka AMD.

%package AMD-fortran
Summary:	Fortran version of AMD library
Summary(pl.UTF-8):	Wersja biblioteki AMD dla programów w Fortranie
Version:	%{amd_ver}
License:	LGPL v2.1+
Group:		Libraries
Provides:	AMD-fortran = %{amd_ver}-%{release}
Obsoletes:	AMD-fortran < 2.4.0-5

%description AMD-fortran
Fortran version of AMD library.

%description AMD-fortran -l pl.UTF-8
Wersja biblioteki AMD dla programów napisanych w Fortranie.

%package AMD-fortran-devel
Summary:	Fortran version of AMD library - development files
Summary(pl.UTF-8):	Wersja biblioteki AMD dla programów w Fortranie - pliki programistyczne
Version:	%{amd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-AMD-fortran = %{amd_ver}-%{release}
Provides:	AMD-fortran-devel = %{amd_ver}-%{release}
Obsoletes:	AMD-fortran-devel < 2.4.0-5

%description AMD-fortran-devel
Fortran version of AMD library - development files.

%description AMD-fortran-devel -l pl.UTF-8
Wersja biblioteki AMD dla programów w Fortranie - pliki
programistyczne.

%package AMD-fortran-static
Summary:	Fortran version of AMD static library
Summary(pl.UTF-8):	Wersja statycznej biblioteki AMD dla programów w Fortranie
Version:	%{amd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-AMD-fortran-devel = %{amd_ver}-%{release}
Provides:	AMD-fortran-static = %{amd_ver}-%{release}
Obsoletes:	AMD-fortran-static < 2.4.0-5

%description AMD-fortran-static
Fortran version of AMD static library.

%description AMD-fortran-static -l pl.UTF-8
Wersja statycznej biblioteki AMD dla programów napisanych w Fortranie.

%package BTF
Summary:	BTF: permutation to block triangular form
Summary(pl.UTF-8):	BTF - permutacja do postaci blokowo trójkątnej
Version:	%{btf_ver}
License:	LGPL v2.1+
Group:		Libraries
Provides:	BTF = %{btf_ver}-%{release}
Obsoletes:	BTF < 1.2.0-3

%description BTF
BTF permutes an unsymmetric matrix (square or rectangular) into its
block upper triangular form (more precisely, it computes a
Dulmage-Mendelsohn decomposition). BTF is required by the KLU package.

%description BTF -l pl.UTF-8
BTF permutuje macierz niesymetryczną (kwadratową lub prostokątną) do
postaci górnej blokowo trójkątnej (ściślej mówiąc, oblicza rozkład
Dulmage'a-Mendelsohna). Pakiet BTF jest wymagany przez pakiet KLU.

%package BTF-devel
Summary:	Header files for BTF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BTF
Version:	%{btf_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-BTF = %{btf_ver}-%{release}
Requires:	%{name}-config = %{suite_ver}-%{release}
Provides:	BTF-devel = %{btf_ver}-%{release}
Obsoletes:	BTF-devel < 1.2.0-3

%description BTF-devel
Header files for BTF library.

%description BTF-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BTF.

%package BTF-static
Summary:	Static BTF library
Summary(pl.UTF-8):	Statyczna biblioteka BTF
Version:	%{btf_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-BTF-devel = %{btf_ver}-%{release}
Provides:	BTF-static = %{btf_ver}-%{release}
Obsoletes:	BTF-static < 1.2.0-3

%description BTF-static
Static BTF library.

%description BTF-static -l pl.UTF-8
Statyczna biblioteka BTF.

%package CAMD
Summary:	CAMD: Constrainted Approximate Minimum Degree
Summary(pl.UTF-8):	CAMD - przybliżony ograniczony algorytm minimalnego stopnia
Version:	%{camd_ver}
License:	LGPL v2.1+
Group:		Libraries
Requires:	SuiteSparse-config-libs = %{suite_ver}-%{release}
Provides:	CAMD = %{camd_ver}-%{release}
Obsoletes:	CAMD < 2.4.0-4

%description CAMD
CAMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting).

%description CAMD -l pl.UTF-8
CAMD to zbiór procedur do porządkowania macierzy rzadkich przed
rozkładem Cholesky'ego (lub do rozkładu LU z obrotami diagonalnymi).

%package CAMD-devel
Summary:	Header files for CAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CAMD
Version:	%{camd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-CAMD = %{camd_ver}-%{release}
Requires:	SuiteSparse-config-devel = %{suite_ver}-%{release}
Provides:	CAMD-devel = %{camd_ver}-%{release}
Obsoletes:	CAMD-devel < 2.4.0-4

%description CAMD-devel
Header files for CAMD library.

%description CAMD-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CAMD.

%package CAMD-static
Summary:	Static CAMD library
Summary(pl.UTF-8):	Statyczna biblioteka CAMD
Version:	%{camd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-CAMD-devel = %{camd_ver}-%{release}
Provides:	CAMD-static = %{camd_ver}-%{release}
Obsoletes:	CAMD-static < 2.4.0-4

%description CAMD-static
Static CAMD library.

%description CAMD-static -l pl.UTF-8
Statyczna biblioteka CAMD.

%package CCOLAMD
Summary:	CCOLAMD: constrained column approximate minimum degree
Summary(pl.UTF-8):	CCOLAMD - przybliżony ograniczony algorytm minimalnego stopnia dla kolumn
Version:	%{ccolamd_ver}
License:	LGPL v2.1+
Group:		Libraries
Provides:	CCOLAMD = %{ccolamd_ver}-%{release}
Obsoletes:	CCOLAMD < 2.9.0-4

%description CCOLAMD
The CCOLAMD column approximate minimum degree ordering algorithm
computes a permutation vector P such that the LU factorization of A
(:,P) tends to be sparser than that of A. The Cholesky factorization
of (A (:,P))'*(A (:,P)) will also tend to be sparser than that of
A'*A. CSYMAMD is a symmetric minimum degree ordering method based on
CCOLAMD, available as a MATLAB-callable function. It constructs a
matrix M such that M'*M has the same pattern as A, and then uses
CCOLAMD to compute a column ordering of M.

%description CCOLAMD -l pl.UTF-8
Przybliżony algorytm porządkowania minimalnego stopnia dla kolumn
CCOLAMD oblicza wektor permutacji P taki, że rozkład LU A (:,P) jest
bardziej rzadki niż A. Rozkład Cholesky'ego (A (:,P))'*(A (:,P)) także
jest rzadszy niż A'*A. CSYMAND to przybliżony algorytm porządkowania
minimalnego stopnia dla macierzy symetrycznych oparty na CCOLAMD,
dostępny jako funkcja do wywołania z MATLAB-a. Tworzy macierz M taką,
że M'*M ma ten sam wzór co A, a następnie używa algorytmu CCOLAMD do
obliczenia porządku kolumn M.

%package CCOLAMD-devel
Summary:	Header files for CCOLAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CCOLAMD
Version:	%{ccolamd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-CCOLAMD = %{ccolamd_ver}-%{release}
Requires:	%{name}-config = %{suite_ver}-%{release}
Provides:	CCOLAMD-devel = %{ccolamd_ver}-%{release}
Obsoletes:	CCOLAMD-devel < 2.9.0-4

%description CCOLAMD-devel
Header files for CCOLAMD library.

%description CCOLAMD-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CCOLAMD.

%package CCOLAMD-static
Summary:	Static CCOLAMD library
Summary(pl.UTF-8):	Statyczna biblioteka CCOLAMD
Version:	%{ccolamd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-CCOLAMD-devel = %{ccolamd_ver}-%{release}
Provides:	CCOLAMD-static = %{ccolamd_ver}-%{release}
Obsoletes:	CCOLAMD-static < 2.9.0-4

%description CCOLAMD-static
Static CCOLAMD library.

%description CCOLAMD-static -l pl.UTF-8
Statyczna biblioteka CCOLAMD.

%package COLAMD
Summary:	COLAMD: column approximate minimum degree
Summary(pl.UTF-8):	COLAMD - przybliżony algorytm minimalnego stopnia dla kolumn
Version:	%{colamd_ver}
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	COLAMD = %{colamd_ver}-%{release}
Obsoletes:	COLAMD < 2.9.0-4
Obsoletes:	colamd < 2.7

%description COLAMD
The COLAMD column approximate minimum degree ordering algorithm
computes a permutation vector P such that the LU factorization of A
(:,P) tends to be sparser than that of A. The Cholesky factorization
of (A (:,P))'*(A (:,P)) will also tend to be sparser than that of
A'*A. SYMAMD is a symmetric minimum degree ordering method based on
COLAMD, available as a MATLAB-callable function. It constructs a
matrix M such that M'*M has the same pattern as A, and then uses
COLAMD to compute a column ordering of M. Colamd and symamd tend to be
faster and generate better orderings than their MATLAB counterparts,
colmmd and symmmd.

%description COLAMD -l pl.UTF-8
Przybliżony algorytm porządkowania minimalnego stopnia dla kolumn
(COLAMD) oblicza wektor permutacji P taki, że rozkład LU A (:,P) jest
bardziej rzadki niż A. Rozkład Cholesky'ego (A (:,P))'*(A (:,P)) także
jest rzadszy niż A'*A. SYMAND to przybliżony algorytm porządkowania
minimalnego stopnia dla macierzy symetrycznych oparty na COLAMD,
dostępny jako funkcja do wywołania z MATLAB-a. Tworzy macierz M taką,
że M'*M ma ten sam wzór co A, a następnie używa algorytmu COLAMD do
obliczenia porządku kolumn M. COLAMD i SYMAMD są szybsze i generują
lepsze uporządkowania niż ich odpowiedniki z MATLAB-a: colmmd i
symmmd.

%package COLAMD-devel
Summary:	Header files for COLAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki COLAMD
Version:	%{colamd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-COLAMD = %{colamd_ver}-%{release}
Requires:	%{name}-config-devel = %{suite_ver}-%{release}
Provides:	COLAMD-devel = %{colamd_ver}-%{release}
Obsoletes:	COLAMD-devel < 2.9.0-4
Obsoletes:	colamd-devel < 2.7

%description COLAMD-devel
Header files for COLAMD library.

%description COLAMD-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki COLAMD.

%package COLAMD-static
Summary:	Static COLAMD library
Summary(pl.UTF-8):	Statyczna biblioteka COLAMD
Version:	%{colamd_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-COLAMD-devel = %{colamd_ver}-%{release}
Provides:	COLAMD-static = %{colamd_ver}-%{release}
Obsoletes:	COLAMD-static < 2.9.0-4
Obsoletes:	colamd-static < 2.7

%description COLAMD-static
Static COLAMD library.

%description COLAMD-static -l pl.UTF-8
Statyczna biblioteka COLAMD.

%package CHOLMOD
Summary:	CHOLMOD: sparse supernodal Cholesky factorization and update/downdate
Summary(pl.UTF-8):	CHOLMOD - rzadki wielowęzłowy rozkład Cholesky'ego z poprawianiem
Version:	%{cholmod_ver}
License:	GPL v2+ (some parts LGPL v2.1+)
Group:		Libraries
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	CHOLMOD = %{cholmod_ver}-%{release}
Obsoletes:	CHOLMOD < 3.0.1-6

%description CHOLMOD
CHOLMOD is a set of ANSI C routines for sparse Cholesky
factorization and update/downdate.

%description CHOLMOD -l pl.UTF-8
CHOLMOD to zbiór procedur ANSI C do rzadkiego rozkładu Cholesky'ego z
poprawianiem.

%package CHOLMOD-devel
Summary:	Header files for CHOLMOD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CHOLMOD
Version:	%{cholmod_ver}
License:	GPL v2+ (some parts LGPL v2.1+)
Group:		Development/Libraries
Requires:	%{name}-config-devel = %{suite_ver}-%{release}
Requires:	%{name}-AMD-devel = %{amd_ver}-%{release}
Requires:	%{name}-CAMD-devel = %{camd_ver}-%{release}
Requires:	%{name}-CCOLAMD-devel = %{ccolamd_ver}-%{release}
Requires:	%{name}-CHOLMOD = %{cholmod_ver}-%{release}
Requires:	%{name}-COLAMD-devel = %{colamd_ver}-%{release}
Requires:	blas-devel
Requires:	lapack-devel
%if %{with metis}
Requires:	metis-devel >= 5
%endif
Provides:	CHOLMOD-devel = %{cholmod_ver}-%{release}
Obsoletes:	CHOLMOD-devel < 3.0.1-6

%description CHOLMOD-devel
Header files for CHOLMOD library.

%description CHOLMOD-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CHOLMOD.

%package CHOLMOD-static
Summary:	Static CHOLMOD library
Summary(pl.UTF-8):	Statyczna biblioteka CHOLMOD
Version:	%{cholmod_ver}
License:	GPL v2+ (some parts LGPL v2.1+)
Group:		Development/Libraries
Requires:	%{name}-CHOLMOD-devel = %{cholmod_ver}-%{release}
Provides:	CHOLMOD-static = %{cholmod_ver}-%{release}
Obsoletes:	CHOLMOD-static < 3.0.1-6

%description CHOLMOD-static
Static CHOLMOD library.

%description CHOLMOD-static -l pl.UTF-8
Statyczna biblioteka CHOLMOD.

%package CXSparse
Summary:	CXSparse: extended version of a concise sparse matrix package
Summary(pl.UTF-8):	CXSparse - rozszerzona wersja zwięzłego pakietu do macierzy rzadkich
Version:	%{cxsparse_ver}
License:	LGPL v2.1+
Group:		Libraries
Provides:	CXSparse = %{cxsparse_ver}-%{release}
Obsoletes:	CXSparse < 0.1

%description CXSparse
CXSparse is an extended version of CSparse - a small yet feature-rich
sparse matrix package, with support for double or complex matrices,
with int or long integers.

%description CXSparse -l pl.UTF-8
CXSparse to rozszerzona wersja CSparse - małego, ale mającego wiele
możliwości pakietu do macierzy rzadkich z obsługą macierzy typu double
i zespolonych, z liczbami int i long.

%package CXSparse-devel
Summary:	Header files for CXSparse library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CXSparse
Version:	%{cxsparse_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-CXSparse = %{cxsparse_ver}-%{release}
Requires:	%{name}-config = %{suite_ver}-%{release}
Provides:	CXSparse-devel = %{cxsparse_ver}-%{release}
Obsoletes:	CXSparse-devel < 0.1

%description CXSparse-devel
Header files for CXSparse library.

%description CXSparse-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CXSparse.

%package CXSparse-static
Summary:	Static CXSparse library
Summary(pl.UTF-8):	Statyczna biblioteka CXSparse
Version:	%{cxsparse_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-CXSparse-devel = %{cxsparse_ver}-%{release}
Provides:	CXSparse-static = %{cxsparse_ver}-%{release}
Obsoletes:	CXSparse-static < 0.1

%description CXSparse-static
Static CXSparse library.

%description CXSparse-static -l pl.UTF-8
Statyczna biblioteka CXSparse.

%package KLU
Summary:	KLU: sparse LU factorization, for circuit simulation
Summary(pl.UTF-8):	KLU - rzadki rozkład LU na potrzeby symulacji obwodów
Version:	%{klu_ver}
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name}-AMD = %{amd_ver}-%{release}
Requires:	%{name}-BTF = %{btf_ver}-%{release}
Requires:	%{name}-COLAMD = %{colamd_ver}-%{release}
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	KLU = %{klu_ver}-%{release}
Obsoletes:	KLU < 1.3.0-3

%description KLU
KLU is a sparse LU factorization algorithm well-suited for use in
circuit simulation.

%description KLU -l pl.UTF-8
KLU to algorytm rozkładu LU macierzy rzadkich dobrze pasujący do
zastosowań w symulacji obwodów.

%package KLU-devel
Summary:	Header files for KLU library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki KLU
Version:	%{klu_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-KLU = %{klu_ver}-%{release}
Requires:	%{name}-AMD-devel = %{amd_ver}-%{release}
Requires:	%{name}-BTF-devel = %{btf_ver}-%{release}
Requires:	%{name}-COLAMD-devel = %{colamd_ver}-%{release}
Requires:	%{name}-config-devel = %{suite_ver}-%{release}
Provides:	KLU-devel = %{klu_ver}-%{release}
Obsoletes:	KLU-devel < 1.3.0-3

%description KLU-devel
Header files for KLU library.

%description KLU-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki KLU.

%package KLU-static
Summary:	Static KLU library
Summary(pl.UTF-8):	Statyczna biblioteka KLU
Version:	%{klu_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-KLU-devel = %{klu_ver}-%{release}
Provides:	KLU-static = %{klu_ver}-%{release}
Obsoletes:	KLU-static < 1.3.0-3

%description KLU-static
Static KLU library.

%description KLU-static -l pl.UTF-8
Statyczna biblioteka KLU.

%package LDL
Summary:	LDL: a simple LDL^T factorization for sparse matrices
Summary(pl.UTF-8):	LDL - prosty rozkład LDL^T dla macierzy rzadkich
Version:	%{ldl_ver}
License:	LGPL v2.1+
Group:		Libraries
Provides:	LDL = %{ldl_ver}-%{release}
Obsoletes:	LDL < 2.2.0-2

%description LDL
LDL is a set of concise routines for factorizing symmetric
positive-definite sparse matrices, with some applicability to
symmetric indefinite matrices. Its primary purpose is to illustrate
much of the basic theory of sparse matrix algorithms in as concise a
code as possible, including an elegant new method of sparse symmetric
factorization that computes the factorization row-by-row but stores it
column-by-column. The entire symbolic and numeric factorization
consists of a total of only 49 lines of code. The package is written
in C, and includes a MATLAB interface.

%description LDL -l pl.UTF-8
LDL to zbiór zwięzłych procedur do dokonywania rozkładów
symetrycznych, dodatnio określonych macierzy rzadkich, z częściową
możliwością stosowania do macierzy symetrycznych nieokreślonych.
Główny cel tych procedur to zademonstrowanie dużej części podstawowej
teorii algorytmów dla macierzy rzadkich w jak najbardziej zwięzłym
kodzie, w tym eleganckiej nowej metody rozkładu symetrycznych macierzy
rzadkich, liczącej rozkład wierszami, ale zapisującej go kolumnami.
Cały rozkład symboliczny i numeryczny składa się z jedynie 49 linii
kodu. Pakiet został napisany w C i zawiera interfejs dla MATLAB-a.

%package LDL-devel
Summary:	Header files for LDL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LDL
Version:	%{ldl_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-LDL = %{ldl_ver}-%{release}
Requires:	%{name}-config = %{suite_ver}-%{release}
Provides:	LDL-devel = %{ldl_ver}-%{release}
Obsoletes:	LDL-devel < 2.2.0-2

%description LDL-devel
Header files for LDL library.

%description LDL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LDL.

%package LDL-static
Summary:	Static LDL library
Summary(pl.UTF-8):	Statyczna biblioteka LDL
Version:	%{ldl_ver}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-LDL-devel = %{ldl_ver}-%{release}
Provides:	LDL-static = %{ldl_ver}-%{release}
Obsoletes:	LDL-static < 2.2.0-2

%description LDL-static
Static LDL library.

%description LDL-static -l pl.UTF-8
Statyczna biblioteka LDL.

%package RBio
Summary:	RBio: read/write matrices in Rutherford/Boeing format
Summary(pl.UTF-8):	RBio: odczyt/zapis macierzy zapisanych w formacie Rutherforda-Boeinga
Version:	%{rbio_ver}
License:	GPL v2+
Group:		Libraries
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	RBio = %{rbio_ver}-%{release}
Obsoletes:	RBio < 2.2.0-2

%description RBio
RBio - MATLAB toolbox for reading/writing sparse matrices in the
Rutherford/Boeing format, and for reading/writing problems in the UF
Sparse Matrix Collection from/to a set of files in a directory.
Version 2.0 is written in C. Older versions were in Fortran.

%description RBio -l pl.UTF-8
RBio to narzędzia MATLAB-a do odczytu/zapisu macierzy rzadkich w
formacie Rutherforda-Boeinga oraz odczytu/zapisu problemów dla
oprogramowania UF Sparse Matrix Collection z/do zbioru plików w
katalogu. Wersja 2.0 została napisana w C; wcześniejsze wersje były w
Fortranie.

%package RBio-devel
Summary:	Header files for RBio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RBio
Version:	%{rbio_ver}
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-RBio = %{rbio_ver}-%{release}
Requires:	%{name}-config-devel = %{suite_ver}-%{release}
Provides:	RBio-devel = %{rbio_ver}-%{release}
Obsoletes:	RBio-devel < 2.2.0-2

%description RBio-devel
Header files for RBio library.

%description RBio-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RBio.

%package RBio-static
Summary:	Static RBio library
Summary(pl.UTF-8):	Statyczna biblioteka RBio
Version:	%{rbio_ver}
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-RBio-devel = %{rbio_ver}-%{release}
Provides:	RBio-static = %{rbio_ver}-%{release}
Obsoletes:	RBio-static < 2.2.0-2

%description RBio-static
Static RBio library.

%description RBio-static -l pl.UTF-8
Statyczna biblioteka RBio.

%package SPQR
Summary:	SuiteSparseQR: multithreaded multifrontal sparse QR factorization
Summary(pl.UTF-8):	SuiteSparseQR - wielowątkowy, wielofrontalny rozkład QR dla macierzy rzadkich
Version:	%{spqr_ver}
License:	GPL v2+
Group:		Libraries
Requires:	%{name}-CHOLMOD = %{cholmod_ver}-%{release}
Requires:	%{name}-config-libs = %{suite_ver}-%{release}
Provides:	SPQR = %{spqr_ver}-%{release}
Obsoletes:	SPQR < 1.3.3-5

%description SPQR
SuiteSparseQR is an implementation of the multifrontal sparse QR
factorization method. Parallelism is exploited both in the BLAS and
across different frontal matrices using Intel's Threading Building
Blocks, a shared-memory programming model for modern multicore
architectures. It can obtain a substantial fraction of the theoretical
peak performance of a multicore computer. The package is written in
C++ with user interfaces for MATLAB, C, and C++.

%description SPQR -l pl.UTF-8
SuiteSparseQR to implementacja wielofrontalnej metody rozkładu QR dla
macierzy rzadkich. Równoległość jest wykorzystywna zarówno w BLAS, jak
i poprzez różne macierze frontalne przy użyciu Threading Building
Blocks Intela - model programowania ze współdzieloną pamięcią dla
architektur wielordzeniowych. Dzięki temu możliwe jest osiągnięcie
znaczącej części teoretycznej maksymalnej wydajności na komputerze
wielordzeniowym. Pakiet jest napisany w C++ z interfejsami dla
MATLAB-a, C i C++.

%package SPQR-devel
Summary:	Header files for SPQR library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SPQR
Version:	%{spqr_ver}
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-CHOLMOD-devel = %{cholmod_ver}-%{release}
Requires:	%{name}-SPQR = %{spqr_ver}-%{release}
Requires:	%{name}-config-devel = %{suite_ver}-%{release}
Requires:	libstdc++-devel
Provides:	SPQR-devel = %{spqr_ver}-%{release}
Obsoletes:	SPQR-devel < 1.3.3-5

%description SPQR-devel
Header files for SPQR library.

%description SPQR-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SPQR.

%package SPQR-static
Summary:	Static SPQR library
Summary(pl.UTF-8):	Statyczna biblioteka SPQR
Version:	%{spqr_ver}
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-SPQR-devel = %{spqr_ver}-%{release}
Provides:	SPQR-static = %{spqr_ver}-%{release}
Obsoletes:	SPQR-static < 1.3.3-5

%description SPQR-static
Static SPQR library.

%description SPQR-static -l pl.UTF-8
Statyczna biblioteka SPQR.

%package UMFPACK
Summary:	UMFPACK: sparse multifrontal LU factorization
Summary(pl.UTF-8):	UMFPACK - wielofrontalny rozkład LU macierzy rzadkich
Version:	%{umfpack_ver}
License:	GPL v2+
Group:		Libraries
Requires:	%{name}-CHOLMOD = %{cholmod_ver}-%{release}
Provides:	UMFPACK = %{umfpack_ver}-%{release}
Obsoletes:	UMFPACK < 5.7.0-7

%description UMFPACK
UMFPACK is a set of routines for solving unsymmetric sparse linear
systems, Ax=b, using the Unsymmetric MultiFrontal method. Written in
ANSI/ISO C, with a MATLAB (Version 6.0 and later) interface. Appears
as a built-in routine (for lu, backslash, and forward slash) in
MATLAB. Includes a MATLAB interface, a C-callable interface, and a
Fortran-callable interface. Note that "UMFPACK" is pronounced in two
syllables, "Umph Pack". It is not "You Em Ef Pack".

%description UMFPACK -l pl.UTF-8
UMFPACK to zbiór procedur do rozwiązywania niesymetrycznych rzadkich
układów równań liniowych Ax=b przy użyciu metody UMF (Unsymmetric
MultiFrontal). Jest napisany w ANSI/ISO C z interfejsem do MATLAB-a
(w wersji 6.0 i nowszych). W MATLAB-ie jest dostępny jako wbudowana
procedura (dla lu, backslasha i slasha). Oprócz interfejsu dla
MATLAB-a dostępny jest interfejs dostępny z C i Fortranu. Uwaga:
"UMFPACK" powinno się wymawiać jako dwie sylaby: "Umf Pak"; nie jako
"U Em Ef Pak".

%package UMFPACK-devel
Summary:	Header files for UMFPACK library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki UMFPACK
Version:	%{umfpack_ver}
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-UMFPACK = %{umfpack_ver}-%{release}
Requires:	%{name}-CHOLMOD-devel = %{cholmod_ver}-%{release}
Requires:	%{name}-config = %{suite_ver}-%{release}
Provides:	UMFPACK-devel = %{umfpack_ver}-%{release}
Obsoletes:	UMFPACK-devel < 5.7.0-7

%description UMFPACK-devel
Header files for UMFPACK library.

%description UMFPACK-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki UMFPACK.

%package UMFPACK-static
Summary:	Static UMFPACK library
Summary(pl.UTF-8):	Statyczna biblioteka UMFPACK
Version:	%{umfpack_ver}
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-UMFPACK-devel = %{umfpack_ver}-%{release}
Provides:	UMFPACK-static = %{umfpack_ver}-%{release}
Obsoletes:	UMFPACK-static < 5.7.0-7

%description UMFPACK-static
Static UMFPACK library.

%description UMFPACK-static -l pl.UTF-8
Statyczna biblioteka UMFPACK.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%ifnarch %{x8664} aarch64 alpha mips64 ppc64 s390x sparc64
%patch3 -p1
%endif

%build
export LD_LIBRARY_PATH=$(pwd)/lib${LD_LIBRARY_PATH+:$LD_LIBRARY_PATH}
%{__make} -j1 \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	F77=gfortran \
	FFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -L$(pwd)/lib" \
	%{!?with_metis:CHOLMOD_CONFIG=-DNPARTITION} \
	CUDA=no \
	%{?with_metis:MY_METIS_LIB=-lmetis MY_METIS_INC=%{_includedir}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/suitesparse,%{_datadir}/misc}

%{__make} -j1 install \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	F77=gfortran \
	FFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -L$RPM_BUILD_ROOT%{_libdir}" \
	CUDA=no \
	INSTALL=$RPM_BUILD_ROOT%{_prefix} \
	INSTALL_INCLUDE=$RPM_BUILD_ROOT%{_includedir}/suitesparse \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
	MY_METIS_LIB=-lmetis

cp -p SuiteSparse_config/SuiteSparse_config.mk $RPM_BUILD_ROOT%{_datadir}/misc
cp -p SuiteSparse_config/lib*.a */Lib/lib*.a $RPM_BUILD_ROOT%{_libdir}
# CXSparse is superset; don't package CSparse
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcsparse.a
# packaged as %doc in individual subpackages
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/suitesparse-%{suite_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	config-libs -p /sbin/ldconfig
%postun	config-libs -p /sbin/ldconfig

%post	AMD -p /sbin/ldconfig
%postun	AMD -p /sbin/ldconfig

%post	BTF -p /sbin/ldconfig
%postun	BTF -p /sbin/ldconfig

%post	CAMD -p /sbin/ldconfig
%postun	CAMD -p /sbin/ldconfig

%post	CCOLAMD -p /sbin/ldconfig
%postun	CCOLAMD -p /sbin/ldconfig

%post	COLAMD -p /sbin/ldconfig
%postun	COLAMD -p /sbin/ldconfig

%post	CHOLMOD -p /sbin/ldconfig
%postun	CHOLMOD -p /sbin/ldconfig

%post	CXSparse -p /sbin/ldconfig
%postun	CXSparse -p /sbin/ldconfig

%post	KLU -p /sbin/ldconfig
%postun	KLU -p /sbin/ldconfig

%post	LDL -p /sbin/ldconfig
%postun	LDL -p /sbin/ldconfig

%post	RBio -p /sbin/ldconfig
%postun	RBio -p /sbin/ldconfig

%post	SPQR -p /sbin/ldconfig
%postun	SPQR -p /sbin/ldconfig

%post	UMFPACK -p /sbin/ldconfig
%postun	UMFPACK -p /sbin/ldconfig

%files config
%defattr(644,root,root,755)
%doc README.txt
%dir %{_includedir}/suitesparse
%{_includedir}/suitesparse/SuiteSparse_config.h
%{_datadir}/misc/SuiteSparse_config.mk

%files config-libs
%defattr(644,root,root,755)
%doc SuiteSparse_config/README.txt
%attr(755,root,root) %{_libdir}/libsuitesparseconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsuitesparseconfig.so.5

%files config-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsuitesparseconfig.so

%files config-static
%defattr(644,root,root,755)
%{_libdir}/libsuitesparseconfig.a

%files AMD
%defattr(644,root,root,755)
%doc AMD/README.txt AMD/Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/libamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libamd.so.2

%files AMD-devel
%defattr(644,root,root,755)
%doc AMD/Doc/AMD_UserGuide.pdf
%attr(755,root,root) %{_libdir}/libamd.so
%{_includedir}/suitesparse/amd.h

%files AMD-static
%defattr(644,root,root,755)
%{_libdir}/libamd.a

%files AMD-fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamdf77.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libamdf77.so.2

%files AMD-fortran-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamdf77.so

%files AMD-fortran-static
%defattr(644,root,root,755)
%{_libdir}/libamdf77.a

%files BTF
%defattr(644,root,root,755)
%doc BTF/README.txt BTF/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libbtf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbtf.so.1

%files BTF-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbtf.so
%{_includedir}/suitesparse/btf.h

%files BTF-static
%defattr(644,root,root,755)
%{_libdir}/libbtf.a

%files CAMD
%defattr(644,root,root,755)
%doc CAMD/README.txt CAMD/Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/libcamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcamd.so.2

%files CAMD-devel
%defattr(644,root,root,755)
%doc CAMD/Doc/CAMD_UserGuide.pdf
%attr(755,root,root) %{_libdir}/libcamd.so
%{_includedir}/suitesparse/camd.h

%files CAMD-static
%defattr(644,root,root,755)
%{_libdir}/libcamd.a

%files CCOLAMD
%defattr(644,root,root,755)
%doc CCOLAMD/README.txt CCOLAMD/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libccolamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libccolamd.so.2

%files CCOLAMD-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libccolamd.so
%{_includedir}/suitesparse/ccolamd.h

%files CCOLAMD-static
%defattr(644,root,root,755)
%{_libdir}/libccolamd.a

%files COLAMD
%defattr(644,root,root,755)
%doc COLAMD/README.txt COLAMD/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libcolamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolamd.so.2

%files COLAMD-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolamd.so
%{_includedir}/suitesparse/colamd.h

%files COLAMD-static
%defattr(644,root,root,755)
%{_libdir}/libcolamd.a

%files CHOLMOD
%defattr(644,root,root,755)
%doc CHOLMOD/README.txt CHOLMOD/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libcholmod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcholmod.so.3

%files CHOLMOD-devel
%defattr(644,root,root,755)
%doc CHOLMOD/Doc/CHOLMOD_UserGuide.pdf
%attr(755,root,root) %{_libdir}/libcholmod.so
%{_includedir}/suitesparse/cholmod*.h

%files CHOLMOD-static
%defattr(644,root,root,755)
%{_libdir}/libcholmod.a

%files CXSparse
%defattr(644,root,root,755)
%doc CXSparse/README.txt CXSparse/Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/libcxsparse.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcxsparse.so.3

%files CXSparse-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcxsparse.so
%{_includedir}/suitesparse/cs.h

%files CXSparse-static
%defattr(644,root,root,755)
%{_libdir}/libcxsparse.a

%files KLU
%defattr(644,root,root,755)
%doc KLU/README.txt KLU/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libklu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libklu.so.1

%files KLU-devel
%defattr(644,root,root,755)
%doc KLU/Doc/{KLU_UserGuide,palamadai_e}.pdf
%attr(755,root,root) %{_libdir}/libklu.so
%{_includedir}/suitesparse/klu.h

%files KLU-static
%defattr(644,root,root,755)
%{_libdir}/libklu.a

%files LDL
%defattr(644,root,root,755)
%doc LDL/README.txt LDL/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libldl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libldl.so.2

%files LDL-devel
%defattr(644,root,root,755)
%doc LDL/Doc/ldl_userguide.pdf
%attr(755,root,root) %{_libdir}/libldl.so
%{_includedir}/suitesparse/ldl.h

%files LDL-static
%defattr(644,root,root,755)
%{_libdir}/libldl.a

%files RBio
%defattr(644,root,root,755)
%doc RBio/README.txt RBio/Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/librbio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librbio.so.2

%files RBio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librbio.so
%{_includedir}/suitesparse/RBio.h

%files RBio-static
%defattr(644,root,root,755)
%{_libdir}/librbio.a

%files SPQR
%defattr(644,root,root,755)
%doc SPQR/README.txt SPQR/Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libspqr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspqr.so.2

%files SPQR-devel
%defattr(644,root,root,755)
%doc SPQR/Doc/{algo_spqr,spqr,spqr_user_guide}.pdf
%attr(755,root,root) %{_libdir}/libspqr.so
%{_includedir}/suitesparse/SuiteSparseQR.hpp
%{_includedir}/suitesparse/SuiteSparseQR*.h
%{_includedir}/suitesparse/spqr.hpp

%files SPQR-static
%defattr(644,root,root,755)
%{_libdir}/libspqr.a

%files UMFPACK
%defattr(644,root,root,755)
%doc UMFPACK/README.txt UMFPACK/Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/libumfpack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libumfpack.so.5

%files UMFPACK-devel
%defattr(644,root,root,755)
%doc UMFPACK/Doc/UMFPACK_{QuickStart,UserGuide}.pdf
%attr(755,root,root) %{_libdir}/libumfpack.so
%{_includedir}/suitesparse/umfpack*.h

%files UMFPACK-static
%defattr(644,root,root,755)
%{_libdir}/libumfpack.a
