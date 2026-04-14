#!/bin/bash

# gpt-4o
# AF

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-4o


# # RF

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-4o


# # NR

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-4o


# # abcd

# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-4o


# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-4o


# gpt-4o COMPARISON

python src/compare_answers.py \
--csv_path results/tables/AF_boolq_gpt-4o_1.csv


python src/compare_answers.py \
--csv_path results/tables/AF_gsm8k_gpt-4o_1.csv


python src/compare_answers.py \
--csv_path results/tables/AF_strategyqa_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/RF_boolq_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/RF_gsm8k_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/RF_strategyqa_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/NR_boolq_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/NR_gsm8k_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/NR_strategyqa_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/AF_abcd_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/RF_abcd_gpt-4o.csv


python src/compare_answers.py \
--csv_path results/tables/NR_abcd_gpt-4o.csv



# gpt-5.4
# AF

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-5.4


# # RF

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-5.4


# # NR

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-5.4


# # abcd

# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant AF \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant RF \
# --model_name gpt-5.4


# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant NR \
# --model_name gpt-5.4



# gpt-5.4 COMPARISON

python src/compare_answers.py \
--csv_path results/tables/AF_boolq_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/AF_gsm8k_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/AF_strategyqa_gpt-5.4.csv



python src/compare_answers.py \
--csv_path results/tables/RF_boolq_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/RF_gsm8k_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/RF_strategyqa_gpt-5.4.csv



python src/compare_answers.py \
--csv_path results/tables/NR_boolq_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/NR_gsm8k_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/NR_strategyqa_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/AF_abcd_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/RF_abcd_gpt-5.4.csv


python src/compare_answers.py \
--csv_path results/tables/NR_abcd_gpt-5.4.csv




# o3
# AF

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant AF \
# --model_name o3 \
# --temperature 1

# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant AF \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant AF \
# --model_name o3 \
# --temperature 1


# # RF

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant RF \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant RF \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant RF \
# --model_name o3 \
# --temperature 1


# # NR

# python src/run_experiments.py \
# --dataset_path data/processed/boolq_validation_seed42_n300.jsonl \
# --variant NR \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/gsm8k_test_seed42_n300.jsonl \
# --variant NR \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/strategyqa_test_seed42_n300.jsonl \
# --variant NR \
# --model_name o3 \
# --temperature 1


# # abcd

# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant AF \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant RF \
# --model_name o3 \
# --temperature 1


# python src/run_experiments.py \
# --dataset_path data/processed/abcd_test_seed42_n300.jsonl \
# --variant NR \
# --model_name o3 \
# --temperature 1



# o3 COMPARISON

python src/compare_answers.py \
--csv_path results/tables/AF_boolq_o3.csv


python src/compare_answers.py \
--csv_path results/tables/AF_gsm8k_o3.csv


python src/compare_answers.py \
--csv_path results/tables/AF_strategyqa_o3.csv


python src/compare_answers.py \
--csv_path results/tables/RF_boolq_o3.csv


python src/compare_answers.py \
--csv_path results/tables/RF_gsm8k_o3.csv


python src/compare_answers.py \
--csv_path results/tables/RF_strategyqa_o3.csv


python src/compare_answers.py \
--csv_path results/tables/NR_boolq_o3.csv


python src/compare_answers.py \
--csv_path results/tables/NR_gsm8k_o3.csv


python src/compare_answers.py \
--csv_path results/tables/NR_strategyqa_o3.csv


python src/compare_answers.py \
--csv_path results/tables/AF_abcd_o3.csv


python src/compare_answers.py \
--csv_path results/tables/RF_abcd_o3.csv


python src/compare_answers.py \
--csv_path results/tables/NR_abcd_o3.csv


python src/compare_answers.py \
--csv_path results/tables/NR_abcd_o3_cleaned.csv