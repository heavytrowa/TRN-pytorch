python main.py moments RGB \
--arch InceptionV3 --num_segments 8 \
--consensus_type TRNmultiscale --batch-size 21 \
--resume pretrain/TRN_moments_RGB_InceptionV3_TRNmultiscale_segment8_best.pth.tar \
--eval-freq 5
