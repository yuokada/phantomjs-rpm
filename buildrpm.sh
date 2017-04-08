#!/bin/bash -x
WORK_DIR=`pwd`
BUILD_NAME=phantomjs
BUILD_SPEC=rpm/${BUILD_NAME}.spec
BUILD_DIR=${WORK_DIR}/rpmbuild
BUILD_NUMBER=${BUILD_NUMBER:=0}

PHANTOMJS_VERSION=${PHANTOMJS_VERSION:=2.1.1}
ARCHIVE_DIR=${WORK_DIR}/${BUILD_NAME}
TGZ_URL="https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2"
TGZ_FILE=${BUILD_NAME}.tar.bz2

/bin/rm    -rf ${BUILD_DIR}
/bin/mkdir -p  ${BUILD_DIR}/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
/bin/mkdir -p  ${BUILD_DIR}/BUILD/${BUILD_NAME}

if [[ ! -e ${TGZ_FILE} ]]; then
  wget -O ${TGZ_FILE} ${TGZ_URL}
fi
/bin/mkdir -p ${ARCHIVE_DIR}{/etc/systemd/system/,/etc/tmpfiles.d/,/etc/gohcs,/var/run/gohcs,/src}

/bin/cp      ${TGZ_FILE} ${BUILD_DIR}/SOURCES
/bin/tar jxf ${TGZ_FILE} --strip=1 -C ${BUILD_DIR}/BUILD/${BUILD_NAME}

/usr/bin/rpmbuild -v \
  --define "version ${PHANTOMJS_VERSION}" \
  --define "release ${BUILD_NUMBER}%{?dist}" \
  --define "_topdir ${BUILD_DIR}" \
  -bb ${BUILD_SPEC}
