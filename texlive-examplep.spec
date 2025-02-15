Name:		texlive-examplep
Version:	55265
Release:	2
Summary:	Verbatim phrases and listings in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/examplep
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/examplep.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/examplep.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Examplep provides sophisticated features for typesetting
verbatim source code listings, including the display of the
source code and its compiled LaTeX or METAPOST output side-by-
side, with automatic width detection and enabled page breaks
(in the source), without the need for specifying the source
twice. Special care is taken that section, page and footnote
numbers do not interfere with the main document. For
typesetting short verbatim phrases, a replacement for the \verb
command is also provided in the package, which can be used
inside tables and moving arguments such as footnotes and
section titles. The listings package is used for syntax
highlighting. The accompanying codep package and the wrfiles.pl
Perl script provide a convenient interface to the examplep
package for authors of manuals. With codep it is possible to
generate the source code, the LaTeX or METAPOST output and the
compilable example file from a single source embedded into the
appropriate place of the .tex document file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/examplep/codep.sty
%{_texmfdistdir}/tex/latex/examplep/examplep.sty
%{_texmfdistdir}/tex/latex/examplep/verbfwr.sty
%doc %{_texmfdistdir}/doc/latex/examplep/README
%doc %{_texmfdistdir}/doc/latex/examplep/eurotex_2005_examplep.pdf
%doc %{_texmfdistdir}/doc/latex/examplep/eurotex_2005_examplep.tex
%doc %{_texmfdistdir}/doc/latex/examplep/houses.eps
%doc %{_texmfdistdir}/doc/latex/examplep/houses.pdf
%doc %{_texmfdistdir}/doc/latex/examplep/pexaminipage.eps
%doc %{_texmfdistdir}/doc/latex/examplep/pexaminipage.pdf
%doc %{_texmfdistdir}/doc/latex/examplep/shorthyp_t1xtts.eps
%doc %{_texmfdistdir}/doc/latex/examplep/shorthyp_t1xtts.pdf
%doc %{_texmfdistdir}/doc/latex/examplep/wrfiles.pl

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
