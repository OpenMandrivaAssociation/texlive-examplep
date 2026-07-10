%global tl_name examplep
%global tl_revision 55265

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04
Release:	%{tl_revision}.1
Summary:	Verbatim phrases and listings in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/examplep
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/examplep.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/examplep.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Examplep provides sophisticated features for typesetting verbatim source
code listings, including the display of the source code and its compiled
LaTeX or MetaPost output side-by-side, with automatic width detection
and enabled page breaks (in the source), without the need for specifying
the source twice. Special care is taken that section, page and footnote
numbers do not interfere with the main document. For typesetting short
verbatim phrases, a replacement for the \verb command is also provided
in the package, which can be used inside tables and moving arguments
such as footnotes and section titles. The listings package is used for
syntax highlighting. The accompanying codep package and the wrfiles.pl
Perl script provide a convenient interface to the examplep package for
authors of manuals. With codep it is possible to generate the source
code, the LaTeX or MetaPost output and the compilable example file from
a single source embedded into the appropriate place of the .tex document
file.

