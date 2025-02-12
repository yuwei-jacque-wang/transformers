# coding=utf-8
# Copyright 2020 The Allen Institute for AI team and The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Longformer configuration """

import logging
from typing import List, Union

from .configuration_roberta import RobertaConfig


logger = logging.getLogger(__name__)

LONGFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "longformer-base-4096": "https://s3.amazonaws.com/models.huggingface.co/bert/allenai/longformer-base-4096/config.json",
    "longformer-large-4096": "https://s3.amazonaws.com/models.huggingface.co/bert/allenai/longformer-large-4096/config.json",
}


class LongformerConfig(RobertaConfig):
    r"""
        This is the configuration class to store the configuration of an :class:`~transformers.LongformerModel`.
        It is used to instantiate an Longformer model according to the specified arguments, defining the model
        architecture. Instantiating a configuration with the defaults will yield a similar configuration to that of
        the RoBERTa `roberta-base <https://huggingface.co/roberta-base>`__ architecture with a sequence length 4,096.

        The :class:`~transformers.LongformerConfig` class directly inherits :class:`~transformers.RobertaConfig`.
        It reuses the same defaults. Please check the parent class for more information.

        Example::

            from transformers import LongformerConfig, LongformerModel

            # Initializing a Longformer configuration
            configuration = LongformerConfig()

            # Initializing a model from the configuration
            model = LongformerModel(configuration)

            # Accessing the model configuration
            configuration = model.config

        Attributes:
            pretrained_config_archive_map (Dict[str, str]):
                A dictionary containing all the available pre-trained checkpoints.
    """
    pretrained_config_archive_map = LONGFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP
    model_type = "longformer"

    def __init__(self, attention_window: Union[List[int], int] = 512, attention_mode: str = "longformer", **kwargs):
        """
        Args:
            attention_window (:obj:`int` or :obj:`List[int]`, optional, defaults to 512):
                Size of an attention window around each token. If :obj:`int`, use the same size for all layers.
                To specify a different window size for each layer, use a :obj:`List[int]` where
                `len(attention_window) == num_hidden_layers`.
            attention_mode (:obj:`str`, optional, possible values ['longformer', 'bert'], defaults to 'longformer'):
                Type of selfattention. Use 'longformer' for :obj:`LongformerSelfAttention` or 'bert' for
                standard BERT full n^2 self attention using :obj:`modeling_bert.BertSelfAttention`. Note that full n^2
                selfattention is supported just for comparison, but it will OOM for long sequences.
        """
        super().__init__(**kwargs)
        self.attention_window = attention_window
        self.attention_mode = attention_mode
