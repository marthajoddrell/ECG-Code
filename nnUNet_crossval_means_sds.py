import os
import json

base_path = "/mnt/wwn-0x50014ee26ba13bde-part2/nnUNet_draft_2/round1_transformations/nnUNet_results/Dataset201_ECGs/nnUNetTrainer__nnUNetPlans__2d"

dice_scores = []

for fold in range(5):
    summary_path = os.path.join(base_path, f"fold_{fold}", "validation", "summary.json")
    
    if os.path.exists(summary_path):
        with open(summary_path) as f:
            data = json.load(f)
            
            # Extract the mean Dice score for fold
            global_dice = data.get("mean", {}).get("1", {}).get("Dice", None)
            
            # Check if global Dice score exists and handle it
            if global_dice is not None:
                fold_scores = [global_dice]
            else:
                fold_scores = []
            
            # Extract Dice scores for individual cases
            for entry in data.get("metric_per_case", []):
                metrics = entry.get("metrics", {}).get("1", {})
                dice_score = metrics.get("Dice", None)
                if dice_score is not None:
                    fold_scores.append(dice_score)
            
            # If we found any scores, calculate mean and std dev for the fold
            if fold_scores:
                mean_dice = sum(fold_scores) / len(fold_scores)
                variance = sum((x - mean_dice) ** 2 for x in fold_scores) / len(fold_scores)
                std_dev_dice = variance ** 0.5
                
                dice_scores.append((fold, mean_dice, std_dev_dice))
            else:
                print(f"⚠️  No valid Dice scores found for fold {fold}.")
    
    else:
        print(f"❌ File not found: {summary_path}")

# Now print the Dice scores per fold and overall statistics
if dice_scores:
    print("📊 Dice Scores per Fold:")
    for fold, mean, std in dice_scores:
        print(f"Fold {fold}: Mean Dice = {mean:.4f}, Std Dev = {std:.4f}")
    
    # Calculate overall mean and std dev
    all_scores = [score[1] for score in dice_scores]
    overall_mean = sum(all_scores) / len(all_scores)
    overall_variance = sum((x - overall_mean) ** 2 for x in all_scores) / len(all_scores)
    overall_std_dev = overall_variance ** 0.5
    
    print(f"\nOverall Mean Dice: {overall_mean:.4f}")
    print(f"Overall Std Dev Dice: {overall_std_dev:.4f}")
else:
    print("❌ No Dice scores were found across all folds.")
