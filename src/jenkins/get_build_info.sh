#!/bin/bash

info_start="=========$(date +%Y-%m-%d_%H:%M:%S)"

info_jobname="JOB_NAME:${JOB_NAME}"
info_branch="Branch:${Branch}"
info_dst_env="Dest_Env:${Dest_Env}"
info_depl_dir="Deploy_dir:${Deploy_dir}"
info_roll="Rollback:${Rollback}"
info_tag="Tag:${Tag}"
info_tag_inp="Input_tag:${Input_Tag}"
info_revision="Revision:${Revision}"
info_revision_inp="Input_Revision:${Input_Revision}"

info_end="Build ${BUILD_NUMBER} completed."


echo -e "${info_start}\n${info_jobname}\n${info_branch}\n${info_dst_env}\n${info_depl_dir}\n${info_roll}\n${info_tag}\n${info_tag_inp}\n${info_revision}\n${info_revision_inp}\n${info_end}\n" >> /tmp/build.txt
