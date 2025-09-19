
%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global _buildhost build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           kube-controller-tools
Version:        0.19.0
Release:        1%{?dist}
Summary:        Tools for writing Kubernetes controllers
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubernetes-sigs/controller-tools
Source:         %{name}-%{version}.tar.bz2

%description
Tools for writing Kubernetes controllers

%prep
%setup -q -n %{name}-%{version}

%build
go build -o controller-gen ./cmd/controller-gen 
go build -o helpgen ./cmd/helpgen
go build -o type-scaffold ./cmd/type-scaffold

%install
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}/%{_bindir} controller-gen
install -p -m 755 -t %{buildroot}/%{_bindir} helpgen
install -p -m 755 -t %{buildroot}/%{_bindir} type-scaffold

%files
%license LICENSE THIRD_PARTY_LICENSES.txt
/usr/bin/controller-gen
/usr/bin/helpgen
/usr/bin/type-scaffold

%changelog
* Fri Sep 19 2025 Olcne-Builder Jenkins <olcne-builder_us@oracle.com> - 0.19.0-1
- Added Oracle specific build files for controller-tools.

