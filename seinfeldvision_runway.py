import runway
import gpt_2_simple as gpt2
from runway.data_types import text

# Setup the model, initialize weights, set the configs of the model, etc.
# Every model will have a different set of configurations and requirements.
# Check https://docs.runwayapp.ai/#/python-sdk to see a complete list of
# supported configs. The setup function should return the model ready to be
# used.
setup_options = {
    'run_name': text(default='first_345m_run'),
}


run_name = None
sess = None

@runway.setup(options=setup_options)
def setup(opts):
    global run_name, sess
    run_name = opts['run_name']
    print(f'Run name: {run_name}')
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=run_name)
    return None

# Every model needs to have at least one command. Every command allows to send
# inputs and process outputs. To see a complete list of supported inputs and
# outputs data types: https://sdk.runwayml.com/en/latest/data_types.html
@runway.command(name='generate',
                inputs={ 'caption': text() },
                outputs={ 'script': text() })
def generate(model, args):
    print('[GENERATE] Ran with caption value "{}"'.format(args['caption']))

    samples = gpt2.generate(sess, nsamples=1, return_as_list=True,
                       prefix=f"({args['caption']})",
                        include_prefix=True, length=200, temperature=0.7,
                       run_name=run_name)
    return {
        'script': samples[0][len(args['caption']):]
    }

if __name__ == '__main__':
    # run the model server using the default network interface and ports,
    # displayed here for convenience
    runway.run(host='127.0.0.1', port=8000,
        model_options={ 'run_name': 'first_345m_run' })