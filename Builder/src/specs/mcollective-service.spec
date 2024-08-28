%global realversion 3.1.2
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>
%global realname mcollective-service-agent

Summary:   Start and stop system services
Name:      EXTRlitpmcollectiveserviceagent_CXP9031039
Version:   %{rpmversion}
Release:   1
Vendor:    PuppetLabs
License:   ASL 2.0
URL:       https://github.com/puppetlabs/mcollective-service-agent
BuildRoot: %{_tmppath}/%{realname}-d2ce4642d56ec72586b03ee51506dc83ca95295a-root-%(%{__id_u} -n)
BuildArch: noarch
Group:     System Tools
Source0:   mcollective-service-agent-%{realversion}.zip
Requires: mcollective-service-common = %{realversion}-%{release}
Provides:  mcollective-service-agent = 3.1.2
Packager:  %{packager}

%description
mcollective-service-agent 3.1.2 repackaged by Ericsson from Puppet Labs source code.

%prep
%setup -q  -n %{realname}-d2ce4642d56ec72586b03ee51506dc83ca95295a

%build

%install
rm -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libexecdir}/mcollective/mcollective
cp -a agent application data util validator %{buildroot}%{_libexecdir}/mcollective/mcollective

%clean
rm -rf %{buildroot}

%package -n EXTRlitpmcollectiveserviceclient_CXP9031356
Requires: mcollective-service-common = %{realversion}-%{release}
Provides: mcollective-service-client = 3.1.2
Group: System Tools
Summary:   Start and stop system services

%package -n EXTRlitpmcollectiveservicecommon_CXP9031357
Requires: mcollective-common >= 2.2.1
Provides: mcollective-service-common = 3.1.2
Group: System Tools
Summary:   Start and stop system services

%description -n EXTRlitpmcollectiveserviceclient_CXP9031356
mcollective-service-client 3.1.2 repackaged by Ericsson from Puppet Labs source code.

%description -n EXTRlitpmcollectiveservicecommon_CXP9031357
mcollective-service-common 3.1.2 repackaged by Ericsson from Puppet Labs source code.

%files
%{_libexecdir}/mcollective/mcollective/agent/*.rb

%files -n EXTRlitpmcollectiveserviceclient_CXP9031356
%{_libexecdir}/mcollective/mcollective/application/*.rb

%files -n EXTRlitpmcollectiveservicecommon_CXP9031357
%{_libexecdir}/mcollective/mcollective/agent/*.ddl
%{_libexecdir}/mcollective/mcollective/data/*
%{_libexecdir}/mcollective/mcollective/util/*
%{_libexecdir}/mcollective/mcollective/validator/*

