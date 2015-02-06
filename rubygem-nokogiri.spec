# Generated from nokogiri-1.5.0.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	nokogiri

Summary:	Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Name:		rubygem-%{rbname}

Version:	1.5.0
Release:	5
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://nokogiri.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
Patch0:		nokogiri-1.5.0-string-format-fix.patch
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	locales-en

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.
XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .str_fmt~

%build
export LC_ALL=en_US.UTF-8
%gem_build

%install
%gem_install

%files
%{_bindir}/nokogiri
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/bin
%dir %{gem_dir}/gems/%{rbname}-%{version}/ext
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/xsd
%{gem_dir}/gems/%{rbname}-%{version}/bin/nokogiri
%dir %{gem_dir}/gems/%{rbname}-%{version}/ext/nokogiri
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/css
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/css/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/css/*.rex
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/css/*.y
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/decorators
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/decorators/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/html
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/html/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/html/sax
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/html/sax/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/node
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/node/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/pp
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/pp/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/sax
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/sax/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/xpath
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/xpath/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xslt
%{gem_dir}/gems/%{rbname}-%{version}/lib/nokogiri/xslt/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/xsd/xmlparser
%{gem_dir}/gems/%{rbname}-%{version}/lib/xsd/xmlparser/*.rb

%{ruby_sitearchdir}/%{rbname}/*.so
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec


%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{gem_dir}/gems/%{rbname}-%{version}/*.txt
%doc %{gem_dir}/gems/%{rbname}-%{version}/ext/nokogiri/*.c
%doc %{gem_dir}/doc/%{rbname}-%{version}


