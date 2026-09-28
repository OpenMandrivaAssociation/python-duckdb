Name:		python-duckdb
Version:	1.4.5
Release:	1
Summary:	DuckDB in-process database
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/duckdb/
Source0:	duckdb-1.4.5.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(scikit-build-core)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gcc-c++
BuildRequires:	lib64python-devel
BuildRequires:	python%{pyver}dist(pybind11)
BuildRequires:	python%{pyver}dist(setuptools-scm)
%description
DuckDB in-process database.

%files
%{python_sitearch}/*
