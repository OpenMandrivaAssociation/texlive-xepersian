# revision 32897
# category Package
# catalog-ctan /macros/xetex/latex/xepersian
# catalog-date 2014-02-04 13:42:17 +0100
# catalog-license lppl1.3
# catalog-version 13.7
Name:		texlive-xepersian
Version:	13.7
Release:	1
Summary:	Persian for LaTeX, using XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xepersian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.source.tar.xz
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
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xepersian/parsidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xepersian/parsidigits.tec
%{_texmfdistdir}/tex/xelatex/xepersian/algorithm-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/algorithmic-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/amsart-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/amsbook-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/article-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/artikel1-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/artikel2-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/artikel3-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/backref-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/bidimoderncv-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/bidituftesidenote-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/boek-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/boek3-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/book-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/bookest-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/breqn-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/color-localise-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/enumerate-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/extarticle-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/extbook-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/extrafootnotefeatures-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/extreport-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/flowfram-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/footnote-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/framed-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/glossaries-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/hyperref-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/imsproc-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/kashida-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/latex-localise-commands-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/latex-localise-environments-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/latex-localise-messages-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/latex-localise-misc-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/listings-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/loadingorder-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/localise-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/memoir-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/minitoc-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/natbib-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/packages-localise-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/rapport1-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/rapport3-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/refrep-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/report-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/scrartcl-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/scrbook-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/scrreprt-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/tkz-linknodes-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/tocloft-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian-localise-commands-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian-localise-environments-xepersian.def
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian-magazine.cls
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian-mathsdigitspec.sty
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian-multiplechoice.sty
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian-persiancal.sty
%{_texmfdistdir}/tex/xelatex/xepersian/xepersian.sty
%doc %{_texmfdistdir}/doc/xelatex/xepersian/README
%doc %{_texmfdistdir}/doc/xelatex/xepersian/ftxe-0.12.py
%doc %{_texmfdistdir}/doc/xelatex/xepersian/img/ireland.jpg
%doc %{_texmfdistdir}/doc/xelatex/xepersian/img/weather/clouds.jpg
%doc %{_texmfdistdir}/doc/xelatex/xepersian/img/weather/rain.jpg
%doc %{_texmfdistdir}/doc/xelatex/xepersian/img/weather/sun.jpg
%doc %{_texmfdistdir}/doc/xelatex/xepersian/magazine-sample.tex
%doc %{_texmfdistdir}/doc/xelatex/xepersian/test-correction.tex
%doc %{_texmfdistdir}/doc/xelatex/xepersian/test-empty-form.tex
%doc %{_texmfdistdir}/doc/xelatex/xepersian/test-question-only.tex
%doc %{_texmfdistdir}/doc/xelatex/xepersian/test-solution-form.tex
%doc %{_texmfdistdir}/doc/xelatex/xepersian/xepersian-logo.pdf
%doc %{_texmfdistdir}/doc/xelatex/xepersian/xepersian-logo.tex
%doc %{_texmfdistdir}/doc/xelatex/xepersian/xepersian.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/xepersian/xepersian.dtx
%doc %{_texmfdistdir}/source/xelatex/xepersian/xepersian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
