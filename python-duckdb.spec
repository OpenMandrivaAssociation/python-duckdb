Name:		python-duckdb
# scikit-build does not leave debug sources rpm can package.
%global debug_package %{nil}
Version:	1.5.6
Release:	1
Summary:	DuckDB in-process database
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/duckdb/
Source0:	duckdb-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(scikit-build-core)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pybind11)
BuildRequires:	python%{pyver}dist(setuptools-scm)
%description
DuckDB in-process database.

%files
%{python_sitearch}/*
