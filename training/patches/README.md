# LLaMA-Factory 补丁

`llamafactory-9a0cfdcc-local.patch` 是本项目当前训练流程依赖的第三方源码补丁。

- 基础仓库：`https://github.com/hiyouga/LLaMA-Factory.git`
- 基础 commit：`9a0cfdccfa234304879f83e0c2c17b5ede8121fe`
- 适用范围：长上下文 DPO 的 label-only/chunked logprob，以及 v1 eval、sequence parallel 和 FSDP2 兼容改动。
- 准备和校验方法：见 [DPO 分块 LogProb 方案说明](../docs/内部文档/DPO分块LogProb方案说明.md)。

更新第三方源码时，先在 LLaMA-Factory checkout 中确认改动，再重新导出补丁：

```bash
git -C ../LLaMA-Factory diff --binary -- src/llamafactory \
  > training/patches/llamafactory-<new-base-short>-local.patch
```

导出后要同步修改 `training/scripts/run_pipeline.py` 中的基础 commit，并重新验证补丁可以在干净 checkout 上应用。
