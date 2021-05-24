@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

set BUILDDIR=build
set SOURCEDIR=source

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)


REM If no params are given goto help

if "%~1" == "" (
	echo "no param_1 supplied"
	goto help
)


REM there shouldn't be space between around =
REM PARAM_1 should be local or web, not html.
set PARAM_1=%1

if %PARAM_1% == local (
	set BUILDDIR=build_local
	set BUILD_NAME=html
	goto build_dir_set
)
if %PARAM_1% == web (
	set BUILDDIR=build
	set BUILD_NAME=html
	goto build_dir_set
)
if %PARAM_1% == html (
	echo select local or web explicitly, for inter-sphinx
	REM BUILD_NAME = html
	goto end
)else (
	REM set BUILD_NAME = %PARAM_1%
	REM for other build format above comment can be removed, but that's not the case now.
	echo %PARAM_1%  is not supported now, select local or web explicitly
	goto end
)

:build_dir_set

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)


REM BUILD_NAME is custom variable, it should be html.

%SPHINXBUILD% -M %BUILD_NAME% %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help

%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
