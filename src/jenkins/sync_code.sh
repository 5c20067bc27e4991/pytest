#!/bin/bash

src_path=$WORKSPACE
dst_path="/tmp/depl_test/"


OLD_IFS=$IFS
IFS=","
arr_deploy_dirs=($Deploy_dir)
IFS=$OLD_IFS

####Rollback
if [ $Rollback == "true" ];then
  [ $Tag ] && ver_tag=$Tag
  [ $Input_Tag ] && ver_tag=$Input_Tag
  [ $Revision ] && ver_tag=$Revision
  [ $Input_Revision ] && ver_tag=$Input_Revision
  [ -z $ver_tag ] && echo "Ver_Tag is empty,deploy aborted!!!"  && exit -1
  echo "Ver_Tag:$ver_tag"
  git checkout $ver_tag
fi


####Sync code
for f in ${arr_deploy_dirs[@]}
do
  rm -rf ${dst_path}/$f
  cp -a ${src_path}/$f ${dst_path}
done


echo "Completed hehehe."
