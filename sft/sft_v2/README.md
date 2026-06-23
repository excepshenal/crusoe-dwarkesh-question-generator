Trained on Crusoe prod.

Datasets:
* `dwarkesh-train-8k-len.jsonl`
* `dwarkesh-val-8k-len.jsonl`

Hyperparams:
```
{
    "batch_size": 64,
    "learning_rate": 0.0001,
    "n_epochs": 3,
    "checkpoint_steps": 25,
    "lora_rank": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.0,
    "warmup_ratio": 0,
    "weight_decay": 0,
}
```