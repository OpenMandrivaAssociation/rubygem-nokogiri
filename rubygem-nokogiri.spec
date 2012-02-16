# Generated from nokogiri-1.5.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	nokogiri

Summary:	Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Name:		rubygem-%{rbname}

Version:	1.5.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://nokogiri.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig(libxml-2.0)

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

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/nokogiri
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/ext
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xsd
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/nokogiri
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/ext/nokogiri
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/css
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/css/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/css/*.rex
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/css/*.y
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/decorators
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/decorators/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/html
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/html/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/html/sax
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/html/sax/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/node
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/node/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/pp
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/pp/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/sax
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/sax/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/xpath
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xml/xpath/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xslt
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/nokogiri/xslt/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xsd/xmlparser
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xsd/xmlparser/*.rb

%{ruby_sitearchdir}/%{rbname}/*.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec


%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/ext/nokogiri/*.c
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
