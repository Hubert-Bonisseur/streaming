# Copyright 2023 MosaicML Streaming authors
# SPDX-License-Identifier: Apache-2.0

"""A streaming WebVid dataset."""

from typing import Any

from streaming.base import StreamingDataset


class StreamingWebVid(StreamingDataset):
    """Streaming WebVid dataset.

    Args:
        local (str): Local dataset directory where shards are cached by split.
        remote (str, optional): Download shards from this remote path or directory. If None, this
            rank and worker's partition of the dataset must all exist locally. Defaults to
            ``None``.
        split (str, optional): Which dataset split to use, if any. Defaults to ``None``.
        shuffle (bool): Whether to iterate over the samples in randomized order. Defaults to
            ``False``.
        predownload (int, optional): Target number of samples ahead to download the shards of while
            iterating. Defaults to ``100_000``.
        keep_zip (bool, optional): Whether to keep or delete the compressed file when
            decompressing downloaded shards. If set to None, keep iff remote is local. Defaults to
            ``None``.
        download_retry (int): Number of download re-attempts before giving up. Defaults to ``2``.
        download_timeout (float): Number of seconds to wait for a shard to download before raising
            an exception. Defaults to ``60``.
        validate_hash (str, optional): Optional hash or checksum algorithm to use to validate
            shards. Defaults to ``None``.
        shuffle_seed (int): Seed for Deterministic data shuffling. Defaults to ``9176``.
        num_canonical_nodes (int, optional): Canonical number of nodes for shuffling with resumption.
            Defaults to ``None``, which is interpreted as the number of nodes of the initial run.
        batch_size (int, optional): Batch size of its DataLoader, which affects how the dataset is
            partitioned over the workers. Defaults to ``None``.
    """

    def __getitem__(self, idx: int) -> Any:
        obj = super().__getitem__(idx)
        # Processing goes here.
        return obj