#!/bin/bash
docker run -it \
-v ~/.aws:/home/glue_user/.aws \
-v "${PWD}":/home/glue_user/workspace/ \
-e AWS_PROFILE="$PROFILE_NAME" \
-e DISABLE_SSL=true \
--rm -p 4040:4040 -p 18080:18080  \
--network host \
--name glue_pyspark amazon/aws-glue-libs:glue_libs_4.0.0_image_01 