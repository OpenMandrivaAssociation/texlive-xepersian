Name:		texlive-xepersian
Version:	64872
Release:	2
Summary:	Persian for LaTeX, using XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xepersian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports Persian typesetting, using the Persian
Modern fonts, by default.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xepersian
%{_texmfdistdir}/tex/xelatex/xepersian
%doc %{_texmfdistdir}/doc/xelatex/xepersian
#- source
%doc %{_texmfdistdir}/source/xelatex/xepersian

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
