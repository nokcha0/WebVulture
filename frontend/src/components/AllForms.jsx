
import AttackSlide from '/src/components/attacklvl';
import ThreadSlide from '/src/components/threads';
import UrlInput from '/src/components/urlinput';
import CmdInput from '/src/components/cmdinput';
import DumpCheck from '/src/components/dumpcheck';
import FlushCheck from '/src/components/flushcheck';
import ButtonComponent from '/src/components/sendbutton'

export default function AllForms()
{
    return (
        <section className="all-forms">
            <div className="slide-container">
                <AttackSlide />
                <ThreadSlide />
            </div>
            <div className="check-container">
                <FlushCheck />
                <DumpCheck />
                <CmdInput />
            </div>

            

        </section>
    )

}